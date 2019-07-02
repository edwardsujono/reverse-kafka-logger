# 2 July 2019
`grep_manager` cannot pass any object referenced to the parallel function.
This is because the file is somehow closed when we passed the reference from the 
parent process to its children.