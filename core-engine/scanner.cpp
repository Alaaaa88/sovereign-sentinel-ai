#include <iostream>
#include <string>

// محرك الفحص الأساسي
void analyze(std::string code) {
    if (code.find("gets(") != std::string::npos) {
        std::cout << "Vulnerability Found: Buffer Overflow" << std::endl;
    }
}

int main() {
    std::string test_code = "gets(buffer);";
    analyze(test_code);
    return 0;
}
