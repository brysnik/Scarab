# Scarab

POC of pythonic build system

Scarab follows couple main principles:

1. Coding is live
2. Cutting corners kills peformance
3. DDD - Debug driven development

Ad1. Everything is defined via code or serializable config files. 

Ad2. There is no UI to configure anything! Only informative status pages. Web api will be used to maintain. This will enable simpicity of the tool itself by slightly raising learing curve. The assumption is that this tool is made by coder for coders to program their automation pipelines.

Ad3. Debugger should be available everywhere! You want to stop pipeline and check app state - just set a trace and check. Debugging ability speeds up work significantly.

