#include "parser.hpp"
#include <sstream>

std::vector<FunctionNode> MicroParser::parse_functions(std::string_view file_content) {
    std::vector<FunctionNode> discovered_functions;
    std::string content_str(file_content);
    std::istringstream stream(content_str);
    std::string line;
    int current_line = 0;

    while (std::getline(stream, line)) {
        current_line++;
        if ((line.find("void ") != std::string::npos || line.find("function ") != std::string::npos || line.find("def ") != std::string::npos) 
            && line.find("(") != std::string::npos) {
            
            bool is_sensitive = (line.find("auth") != std::string::npos || 
                                 line.find("login") != std::string::npos || 
                                 line.find("crypto") != std::string::npos);

            discovered_functions.push_back({
                .name = "Func_Line_" + std::to_string(current_line),
                .return_type = "auto",
                .line_number = current_line,
                .is_security_sensitive = is_sensitive
            });
        }
    }
    return discovered_functions;
}
