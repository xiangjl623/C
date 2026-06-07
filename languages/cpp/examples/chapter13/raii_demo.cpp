#include <iostream>
#include <fstream>
#include <string>

class FileGuard {
    std::string path;

public:
    FileGuard(const std::string& p) : path(p) {
        std::cout << "打开文件：" << path << std::endl;
    }
    ~FileGuard() {
        std::cout << "关闭文件：" << path << std::endl;
    }
};

int main() {
    {
        FileGuard guard("data.txt");
        std::cout << "处理文件中..." << std::endl;
    }
    std::cout << "离开作用域，文件已自动关闭" << std::endl;
    return 0;
}
