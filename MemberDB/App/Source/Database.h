#pragma once

#include <string>
#include <vector>
#include <sqlite3.h>

/**
 * This class will act as our abstraction layer, sitting between
 * the application and the underlying database.
 */
class Database
{
public:
	Database();
	virtual ~Database();

	struct MemberRecord
	{
		std::string firstName;
		std::string lastName;
		std::string notes;
		int64_t lastSacramentPrayDate;
	};

	bool Open();
	bool Close();
	bool UpdateRecord(const MemberRecord& record);
	bool GetAllWhoHaveNotPrayedInSacramentMeeting(std::vector<MemberRecord>& recordArray);
	bool GetAllWhoHavePrayedInSacraementMeeting(std::vector<MemberRecord>& recordArray);

	const std::string& GetLastError() const;

private:

	std::string lastError;
	sqlite3* database;
};