# Scarab

POC of distriburted  build system

### Scarab main principles:

1. **Coding is live**. Everything is defined via code or serializable config files.
2. **Cutting corners kills peformance**. There is no UI to configure anything! Only informative status pages. Web api will be used to maintain. This will enable simpicity of the tool itself by slightly raising learing curve. The assumption is that this tool is made by coder for coders to program their automation pipelines. 
3. **DDD - Debug driven development**. Debugger should be available everywhere! You want to stop pipeline and check app state - just set a trace and check. Debugging ability speeds up work significantly.

### Basics of design

Scarab backend is coded in Rust to provide as much performance as possible. Automation pipelines are using python to run to simplify and speed up development.  