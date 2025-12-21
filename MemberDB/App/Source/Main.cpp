#include <QApplication>
#include <QLabel>

int main(int argc, char** argv)
{
#if _DEBUG
	QCoreApplication::addLibraryPath(R"(D:\git_repos\vcpkg\installed\x64-windows\debug\Qt6\plugins)");
#else
	QCoreApplication::addLibraryPath(R"(D:\git_repos\vcpkg\installed\x64-windows\Qt6\plugins)");
#endif

	QApplication app(argc, argv);
	QLabel label;
	label.setText("Hello!");
	label.show();
	
	return app.exec();
}