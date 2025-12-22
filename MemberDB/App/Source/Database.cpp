#include "Database.h"

Database::Database()
{
	this->database = nullptr;
}

/*virtual*/ Database::~Database()
{
	this->Close();
}

const std::string& Database::GetLastError() const
{
	return this->lastError;
}

bool Database::Open()
{
	if (this->database != nullptr)
	{
		this->lastError = "Database alreay open!";
		return false;
	}

	int retCode = sqlite3_open_v2("D:/git_repos/mp3w-clerk-role/MemberDB/Members.db", &this->database, SQLITE_OPEN_READWRITE | SQLITE_OPEN_CREATE, nullptr);
	if (retCode != SQLITE_OK)
	{
		this->lastError = sqlite3_errmsg(this->database);
		sqlite3_close(this->database);
		this->database = nullptr;
		return false;
	}

	const char* createTableSQL = R"(
		CREATE TABLE IF NOT EXISTS Members (
			id INTEGER PRIMARY KEY,
			first_name TEXT NOT NULL,
			last_name TEXT NOT NULL,
			last_sac_pray_date INTEGER,
			notes TEXT,
			UNIQUE (first_name, last_name)
		);
)";

	retCode = sqlite3_exec(this->database, createTableSQL, nullptr, nullptr, nullptr);
	if (retCode != SQLITE_OK)
	{
		this->lastError = "Failed to ensure table exists.";
		return false;
	}

	return true;
}

bool Database::Close()
{
	if (!this->database)
	{
		this->lastError = "Database not open!";
		return false;
	}

	sqlite3_close(this->database);
	this->database = nullptr;
	return true;
}

bool Database::UpdateRecord(const MemberRecord& record)
{
	bool success = false;
	sqlite3_stmt* insertStatement = nullptr;

	do
	{
		const char* insertSQL = R"(
		INSERT INTO Members(first_name, last_name, notes, last_sac_pray_date)
			VALUES(?, ?, ?, ?)
			ON CONFLICT(first_name, clast_name)
			DO UPDATE SET 
				first_name = excluded.first_name,
				last_name = excluded.last_name,
				notes = excluded.notes,
				last_sac_pray_date = excluded.last_sac_pray_date;
)";

		int retCode = sqlite3_prepare_v2(this->database, insertSQL, -1, &insertStatement, nullptr);
		if (retCode != SQLITE_OK)
		{
			this->lastError = "Failed to prepare insert statement!";
			break;
		}

		sqlite3_bind_text(insertStatement, 1, record.firstName.c_str(), -1, SQLITE_STATIC);
		sqlite3_bind_text(insertStatement, 2, record.lastName.c_str(), -1, SQLITE_STATIC);
		sqlite3_bind_text(insertStatement, 3, record.notes.c_str(), -1, SQLITE_STATIC);
		sqlite3_bind_int64(insertStatement, 4, record.lastSacramentPrayDate);

		retCode = sqlite3_step(insertStatement);
		if (retCode != SQLITE_OK)
		{
			this->lastError = sqlite3_errmsg(this->database);
			break;
		}

		success = true;
	} while (false);

	if (insertStatement)
	{
		sqlite3_finalize(insertStatement);
		insertStatement = nullptr;
	}

	return success;
}

bool Database::GetAllWhoHaveNotPrayedInSacramentMeeting(std::vector<MemberRecord>& recordArray)
{
	return false;
}

bool Database::GetAllWhoHavePrayedInSacraementMeeting(std::vector<MemberRecord>& recordArray)
{
	return false;
}