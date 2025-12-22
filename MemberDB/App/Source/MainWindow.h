#pragma once

#include <qmainwindow.h>
#include "Database.h"

class MainWindow : public QMainWindow
{
public:
	MainWindow(QWidget* parentWidget);
	virtual ~MainWindow();

private:
	Database database;
};