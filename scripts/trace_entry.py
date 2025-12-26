import sample.__main__
import inspect

print("🔍 main() is from:", inspect.getfile(sample.__main__.main))
print("🔍 Source code of main():")
print(inspect.getsource(sample.__main__.main))

sample.__main__.main()
