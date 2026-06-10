
# pywin32-stubs

> **⚠️ DEPRECATED**
>
> This package is no longer maintained. Use the official stubs package instead:
>
> ```shell
> pip install types-pywin32
> ```
>
> See: <https://pypi.org/project/types-pywin32/>


## TO @Avasam

> I'm truly grateful to Avasam for occasionally maintaining this side project over the years. This project was never meant to be serious. A few years ago, I was learning and exploring pywin32 to implement some undocumented and unencapsulated features on the Windows platform. Back then, I found pywin32 really cumbersome to use due to the lack of type hints and code suggestions.
> I had to constantly refer to win32api.chm while troubleshooting issues. What's more, win32api.chm is quite outdated, and much of its documentation has never been updated. Given that situation, I thought: "Since win32api.chm is already available, I might as well export it as HTML, crawl the documentation with a web scraper, and generate stub files for my own use."
> That was how this little project came into being.
>
> To be honest, my Python skills were pretty limited when I started this project. I had no experience developing software packages, and package management tools back then were nowhere near as mature as today's Poetry and uv.
> So the project structure was put together rather casually, but it still works well, haha 😂. It managed to generate stubs for nearly all parts of pywin32, though a small number of API documents are outdated and inconsistent with the actual implementations.
>
> This project was created back in 2020, and it's now 2026 — six years have passed. I haven't been involved in its development for a long time, as I moved on to other things. I rarely use or work on pywin32 anymore.
> I never expected Avasam to come across this casual project 🤣. He seems far more motivated than I am to improve the pywin32 stubs 🤔. After he submitted his first pull request, I invited him to be the main maintainer.
> In effect, Avasam has fully taken over this project.
>
> Avasam has made two remarkable contributions:
> 1. He refined the project based on the original codebase and pushed a more complete version to typeshed, making it the official release.
> 2. Over the past six years, he has continuously revised errors and fixed numerous outdated API signatures.
>
> Now you can use the official win32 stubs directly via `typeshed`, or install them with `pip install types-pywin32`.
>
> What began as a casual side project has now fulfilled its purpose. Thank you so much for all your hard work, Avasam.
>
> It is 08:23 Beijing Time on June 10, 2026. As the project owner, I, kaluluosi, have decided to archive this project and remove the `win32-stub` package from PyPI to prevent future developers from confusing it with the official package.
> Thank you again, Avasam. Hope our paths cross again someday.
>
> The end.

>非常感谢Avasam这些年来还偶尔维护这个玩具项目。 这个项目本来就是个玩具，我在几年前研究学习pywin32，用来实现windows平台的一些没有公开和封装的功能的时候，深感pywin32没有typing和提示非常难用。
>一边查win32api.chm一边还要试错。而且pywin32api.chm本身就年代久远，很多为文档都没有更新。在这种情况下，我决定“既然pywin32api.chm就在那里，干脆导出html用爬虫把里面的文档爬出来做成stub自己用吧。”
>于是乎这个玩具项目就诞生了。
>
>不过这个项目诞生的时候，我的python技术其实并不好。主要是没有开发过package，当时包管理工具也没有现在这么完善，哪像现在有poetry和uv。
>这个项目组织结构上就比较随意。不过至少能用。 哈哈😂。 相对还是全面的将pywin32的stub都生成出来，有少数api文档过时跟实际对不上。
>
>这个项目2020年创建，现在2026年了，六年了。其实我都没参与了，因为我转向别的事情去了。主要因为pywin32我后来很少会用到没去研究了。
>我没想到Avasam看到了这个玩具项目🤣，并且他似乎对pywin32的stub的完善比我还有动力🤔，于是乎第一个pr后我就邀请他作为主要维护者。
>事实上Avasam可以说是直接接收了这个玩具项目。
>
>Avasam有两个贡献很伟大：
>1. 他基于这个项目整理了个跟完善的版本 push到了 typeshed，成为了官方版本。
>2. 6年来陆陆续续的做了勘误修正了不少api的过时签名。
>
>现在，你可以直接`typeshed`，或者`pip install types-pywin32`享受到官方背书的 win32 stub。
>
>这个项目，从一个玩具项目开始，到现在完成了它的历史使命。非常感谢Avasam的付出。
>
>现在是2026年6月10日 08点23分 北京时间。项目owner，我 kaluluosi，决定归档此项目，然后pypi上撤掉`win32-stub`这个包避免以后的程序员与官方包混淆。
>Avasam，非常感谢你的付出。我们有缘还会相遇。
>至此。



pywin32-stubs is generated from pywin32.chm, it contains:

- win32-stubs
- win32comext-stubs
- pythonwin-stubs
- win32helper : this package defines win32typing and constants.

vscode uninstalled stubs
![image](https://user-images.githubusercontent.com/1620585/187332660-19fab0a8-899a-4c3b-bdfa-e581312876f5.png)

vscode installed stubs
![image](https://user-images.githubusercontent.com/1620585/187332828-3903b028-e4a8-4ad1-b6b7-9d98966514d5.png)

## Installation

> **Deprecated.** Use [`types-pywin32`](https://pypi.org/project/types-pywin32/) instead.

```shell
pip install pywin32-stubs
```

## Usage

```python
import win32gui
import win32helper.win32con as con

win32gui.MessageBox(0, "hello", 'world', con.MB_OK)

```
