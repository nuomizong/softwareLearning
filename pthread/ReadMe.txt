

1. Download (header, lib and dll) from homepage.

2. 32-bit version lib and dll for MSVC are (pthreadVC2.dll) and (pthreadVC2.lib).

3. Copy headers to the VC include file.

4. Copy lib to the VC lib file.

5. Copy dll to the system path, such as (C:\Windows\SysWOW64).

6. Add <#pragma comment(lib, "pthreadVC2.lib")> in the cpp file.

7. Done and enjoy!