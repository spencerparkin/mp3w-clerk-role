#include <QApplication>
#include "MainWindow.h"

int main(int argc, char** argv)
{
#if _DEBUG
	QCoreApplication::addLibraryPath(R"(D:\git_repos\vcpkg\installed\x64-windows\debug\Qt6\plugins)");
#else
	QCoreApplication::addLibraryPath(R"(D:\git_repos\vcpkg\installed\x64-windows\Qt6\plugins)");
#endif

	QApplication app(argc, argv);

	MainWindow mainWindow(nullptr);
	mainWindow.resize(1200, 800);
	mainWindow.show();
	
	return app.exec();
}