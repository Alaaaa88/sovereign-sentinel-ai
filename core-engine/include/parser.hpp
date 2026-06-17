#pragma once
#include <string>
#include <vector>
#include <concepts>
#include <string_view>

struct FunctionNode {
    std::string name;
    std::string return_type;
    int line_number;
    bool is_security_sensitive;
};

template<typename T>
concept CodeParser = requires(T parser, std::string_view file_content) {
    { parser.parse_functions(file_content) } -> std::same_as<std::vector<FunctionNode>>;
};

class MicroParser {
public:
    std::vector<FunctionNode> parse_functions(std::string_view file_content);
};
