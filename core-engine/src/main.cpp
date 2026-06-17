#include <iostream>
#include <memory>
#include <concepts>
#include <sstream>
#include "parser.hpp"

int main() {
    std::stringstream buffer;
    buffer << std::cin.rdbuf();
    std::string target_source_code = buffer.str();

    static_assert(AdvancedCodeAnalyzer<SovereignParser>, "SovereignParser must meet AdvancedCodeAnalyzer constraints");

    auto analyzer = std::make_unique<SovereignParser>();
    auto results = analyzer->analyze_codebase(target_source_code);

    nlohmann::json output_json = analyzer->serialize_to_json(results, "dynamic_input.cpp");
    
    std::cout << output_json.dump() << std::endl;

    return 0;
}