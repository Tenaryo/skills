# Review Criteria - C++ Code Review Detailed Standards

各审查维度的详细检查清单和评估标准。

## Table of Contents

- [1. Performance (性能)](#1-performance)
- [2. Modern C++ Style (现代C++风格)](#2-modern-c-style)
- [3. Safety (安全性)](#3-safety)
- [4. Extensibility (可扩展性)](#4-extensibility)
- [5. Code Quality (代码质量)](#5-code-quality)
- [6. Build System & Config (构建系统与项目配置)](#6-build-system--config)

---

## 1. Performance

### 1.1 内存分配

- [ ] 是否存在热路径上的频繁堆分配（`new`, `malloc`, `std::vector::push_back` 未 reserve）
- [ ] 字符串拼接是否使用 `std::string::reserve` 或 `std::ostringstream`
- [ ] 容器是否预知大小并调用了 `reserve()`
- [ ] 是否可用对象池或自定义分配器替代频繁分配
- [ ] 小对象是否使用 `std::optional` 或栈分配替代堆分配

### 1.2 不必要的拷贝

- [ ] 函数参数是否使用了不必要的值传递（应使用 `const&` 或 `string_view`）
- [ ] 返回值是否使用了不必要的拷贝（应依赖 RVO 或返回 `&&`）
- [ ] 是否有可替换为移动语义的拷贝操作
- [ ] range-for 循环中是否使用了不必要的拷贝 `for (auto x : vec)` 应改为 `for (const auto& x : vec)`

### 1.3 缓存友好性

- [ ] 数据结构是否是 SoA vs AoS 的合理选择
- [ ] 热路径数据是否紧凑排列（避免 cache miss）
- [ ] 是否有不必要的虚函数调用（虚表指针导致缓存行失效）
- [ ] 多线程访问的数据是否避免了 false sharing

### 1.4 算法复杂度

- [ ] 是否有 O(n²) 可优化为 O(n log n) 或 O(n) 的算法
- [ ] 查找操作是否使用了合适的容器（`unordered_map` vs `map`）
- [ ] 排序后是否可以用二分查找替代线性查找
- [ ] 循环中是否有不变量的重复计算

### 1.5 编译期计算

- [ ] 常量是否可用 `constexpr` 或 `consteval`
- [ ] 模板元编程是否可替代运行时分支
- [ ] 查找表是否可编译期生成
- [ ] `if constexpr` 是否可替代 SFINAE 或运行时 if

## 2. Modern C++ Style

### 2.1 C++17 特性

- [ ] `std::optional` 替代指针表示可能缺失的值
- [ ] `std::variant` 替代联合体或类型标签枚举
- [ ] `std::string_view` 替代 `const std::string&` 参数
- [ ] 结构化绑定 `auto [key, value] = pair`
- [ ] `if constexpr` 替代 SFINAE
- [ ] `std::filesystem` 替代平台特定的文件操作
- [ ] 折叠表达式替代递归模板

### 2.2 C++20 特性

- [ ] Concepts 替代 SFINAE 和 `static_assert`
- [ ] Ranges 替代手写循环和 `<algorithm>` 组合
- [ ] Coroutines 用于异步代码简化
- [ ] `std::format` 替代 `sprintf` / `std::stringstream`
- [ ] 三路比较运算符 `<=>`
- [ ] `consteval` 和 `constinit`
- [ ] `std::span` 替代指针+长度参数对
- [ ] 指定初始化器 `Named{.x=1, .y=2}`

### 2.3 C++23/26 特性

- [ ] `std::expected` 替代异常或错误码（C++23）
- [ ] `std::print` 替代 `std::cout` / `printf`（C++23）
- [ ] `std::flat_map` / `std::flat_set` 替代小数据量的 map/set（C++23）
- [ ] `std::generator` 用于协程生成器（C++23）
- [ ] Deducing `this` 綈除 const/non-const 成员函数重复（C++23）
- [ ] `std::simd` 数据并行（C++26）
- [ ] 反射（Reflection）元编程（C++26）

### 2.4 通用现代风格

- [ ] 智能指针替代裸指针（`unique_ptr`, `shared_ptr`）
- [ ] RAII 管理所有资源
- [ ] 枚举使用 `enum class` 而非 `enum`
- [ ] `auto` 推导类型（但不滥用）
- [ ] `[[nodiscard]]`, `[[deprecated]]` 等属性标注
- [ ] `std::make_unique` / `std::make_shared` 替代 `new`

## 3. Safety

### 3.1 内存安全

- [ ] 是否存在悬空指针或悬空引用
- [ ] 是否存在 use-after-free
- [ ] 是否存在数组越界访问（应使用 `at()` 或边界检查）
- [ ] 是否存在未初始化的变量
- [ ] 是否存在内存泄漏（`new` 无对应 `delete`）
- [ ] 智能指针是否避免了循环引用

### 3.2 类型安全

- [ ] 是否存在 C 风格强制转换（应用 `static_cast` 等）
- [ ] 是否存在 `void*` 的不当使用
- [ ] 是否存在隐式类型转换导致的精度丢失
- [ ] `reinterpret_cast` 是否确实必要

### 3.3 并发安全

- [ ] 共享数据是否正确加锁
- [ ] 锁的粒度是否合理（不宜过粗或过细）
- [ ] 是否存在死锁风险（锁的获取顺序）
- [ ] 是否存在数据竞争
- [ ] 原子操作是否使用了正确的 memory order

### 3.4 异常安全

- [ ] 析构函数是否 `noexcept`
- [ ] 是否提供了基本异常安全保证
- [ ] 资源获取是否在构造函数中完成（RAII）
- [ ] 移动构造/移动赋值是否 `noexcept`

### 3.5 输入验证

- [ ] 外部输入是否有边界检查
- [ ] 文件路径是否有路径遍历检查
- [ ] 整数运算是否有溢出检查

## 4. Extensibility

### 4.1 模块化

- [ ] 模块职责是否单一明确
- [ ] 模块间依赖是否最小化
- [ ] 头文件是否使用了前向声明减少编译依赖
- [ ] 是否使用了 Pimpl 模式隐藏实现细节

### 4.2 开放-封闭原则

- [ ] 新功能是否可以通过扩展而非修改现有代码添加
- [ ] 是否使用了策略模式、模板方法等消除条件分支
- [ ] 回调/观察者是否替代了紧耦合的调用

### 4.3 配置化

- [ ] 硬编码值是否可提取为配置参数
- [ ] 平台相关代码是否通过抽象隔离
- [ ] 魔法数字是否提取为命名常量

### 4.4 接口设计

- [ ] 接口是否最小化（接口隔离原则）
- [ ] 接口是否稳定，不因实现变化而变化
- [ ] 是否存在过度设计（YAGNI）

## 5. Code Quality

### 5.1 重复代码

- [ ] 是否存在复制粘贴的代码（应提取为公共函数）
- [ ] 相似逻辑是否可通过模板或泛型统一
- [ ] 是否有可通过继承或组合消除的重复

### 5.2 函数复杂度

- [ ] 单函数是否超过 100 行（应拆分）
- [ ] 嵌套层级是否过深（超过 3 层应重构）
- [ ] 圈复杂度是否过高（超过 10 应重构）
- [ ] 参数数量是否过多（超过 4 个应使用结构体）

### 5.3 命名规范

- [ ] 变量名是否清晰表达意图
- [ ] 函数名是否是动词或动词短语
- [ ] 类型名是否是名词
- [ ] 命名是否与代码库中现有风格一致
- [ ] 是否避免了缩写（除公认的如 `idx`, `ptr`, `len`）

### 5.4 注释质量

- [ ] 注释是否解释"为什么"而非"做了什么"
- [ ] 是否存在过时或误导性注释
- [ ] TODO 注释是否有关联的 issue 或时间表
- [ ] 公共 API 是否有文档注释

### 5.5 文件组织

- [ ] 头文件是否有 include guards 或 `#pragma once`
- [ ] 是否使用了前向声明减少头文件依赖
- [ ] 每个文件是否职责单一
- [ ] 头文件包含顺序是否规范（本项目 → 第三方 → 标准库）

## 6. Build System & Config

### 6.1 CMakeLists.txt

- [ ] CMake 最低版本是否合理（是否过于陈旧或过于激进）
- [ ] 项目名称、版本号、语言标准是否正确设置
- [ ] C++ 标准是否通过 `CMAKE_CXX_STANDARD` 或 `target_compile_features` 正确指定
- [ ] 是否使用了过时的 CMake 命令（如 `aux_source_directory`、`glob` 替代手动列举源文件）
- [ ] target-based 方式管理依赖（`target_link_libraries`、`target_include_directories`）是否替代了全局 `include_directories`/`link_libraries`
- [ ] 是否使用了 `PUBLIC/PRIVATE/INTERFACE` 正确控制传递性
- [ ] 编译选项是否通过 `target_compile_options` 或 generator expression 精确控制（而非全局 `add_definitions` / `CMAKE_CXX_FLAGS`）
- [ ] 是否使用了现代 CMake 特性（如 `FetchContent` 替代 `ExternalProject_Add`）
- [ ] find_package 是否指定了具体版本和 COMPONENTS
- [ ] install 规则是否完善（库、头文件、CMake 配置文件）
- [ ] 是否有不必要的硬编码路径
- [ ] 是否正确处理了平台差异（通过 generator expression 或条件判断）
- [ ] 测试是否通过 CTest 集成（`enable_testing()` + `add_test()`）
- [ ] 是否有未使用的变量或冗余的 find_package

### 6.2 编译选项与警告

- [ ] 是否启用了合理的警告级别（`-Wall -Wextra -Wpedantic` 或 `/W4`）
- [ ] 是否将警告视为错误（`-Werror`）— 对持续集成质量至关重要
- [ ] 是否启用了 sanitizers（`-fsanitize=address,undefined` 用于 Debug 构建）
- [ ] Debug/Release 构建类型是否正确区分优化级别
- [ ] 是否启用了 LTO（Link Time Optimization）用于 Release 构建
- [ ] 是否设置了合理的 `-march` 标志（如 `-march=native` 或目标平台架构）
- [ ] 是否有未使用的编译选项或重复定义

### 6.3 依赖管理

- [ ] 第三方依赖版本是否锁定（vcpkg 的 `baseline`、conan 的 `lockfile`、FetchContent 的 `GIT_TAG`）
- [ ] 是否有不必要的依赖（可用标准库或轻量替代品替换）
- [ ] 依赖是否以 source 方式引入但应改为系统包或反之
- [ ] git submodule 路径是否合理，是否有未使用的 submodule
- [ ] 依赖许可证是否兼容项目许可证

### 6.4 CI/CD 配置

- [ ] 是否在多个编译器（GCC、Clang、MSVC）上测试
- [ ] 是否在多个平台（Linux、macOS、Windows）上测试（如项目需要跨平台）
- [ ] 是否有缓存策略（ccache、构建缓存）加速 CI
- [ ] 是否使用了 matrix build 覆盖不同配置
- [ ] 是否有 Release/Debug 两种构建类型的测试
- [ ] 是否自动化了代码质量检查（clang-tidy、cppcheck、clang-format）
- [ ] Artifacts（二进制、测试报告）是否正确归档

### 6.5 代码格式化与静态分析

- [ ] 是否存在 `.clang-format` 配置文件，且风格与实际代码一致
- [ ] 是否存在 `.clang-tidy` 配置文件，检查规则是否合理
- [ ] 是否存在 `compile_commands.json` 生成步骤（供工具链使用）
- [ ] 格式化和静态分析是否集成到 CI 或 pre-commit hook
