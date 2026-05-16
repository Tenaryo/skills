# Naming Conventions

Follow these naming conventions for all C++ identifiers:

| Category | Case | Prefix/Suffix | Example |
|---|---|---|---|
| Classes | PascalCase | — | `HttpClient`, `FileManager` |
| Structs | PascalCase | — | `Point`, `BufferView` |
| Functions | snake_case | — | `parse_input`, `get_connection` |
| Methods | snake_case | — | `start_service`, `is_ready` |
| Variables | snake_case | — | `buffer`, `max_count` |
| Local variables | snake_case | — | `result`, `temp_buffer` |
| Member variables | snake_case | trailing `_` | `count_`, `data_ptr_` |
| Constants | PascalCase | prefix `k` | `kMaxSize`, `kDefaultTimeout` |
| Template parameters | PascalCase | — | `T`, `Allocator`, `KeyType` |

# Build

```sh
./build.sh            # Debug build (default)
./build.sh Release    # Release build
```

# Test

```sh
./run_tests.sh
```
