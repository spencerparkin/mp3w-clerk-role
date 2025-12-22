#include "MainWindow.h"

MainWindow::MainWindow(QWidget* parentWidget) : QMainWindow(parentWidget)
{
	this->database.Open();
}

/*virtual*/ MainWindow::~MainWindow()
{
	this->database.Close();
}