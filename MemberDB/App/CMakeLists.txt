# CMakeLists.txt for the MemberDB app.

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

find_package(Qt6 CONFIG REQUIRED COMPONENTS Widgets REQUIRED)

add_executable(MemberDB
	Source/Main.cpp
	Source/Database.cpp
	Source/Database.h
	Source/MainWindow.cpp
	Source/MainWindow.h
)

target_link_libraries(MemberDB PRIVATE
	Qt6::Widgets
	sqlite3
)