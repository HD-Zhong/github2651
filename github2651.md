github网址：

https://github.com/HD-Zhong/github2651

# 初始化本地仓库

git init

# 添加全部文件

git add .

# 提交文件并写备注

git commit -m "首次提交项目"

# 绑定云端仓库（粘贴刚才复制的链接）

git remote add origin 仓库链接（仓库名要和云端一致）

# 推送到云端

git push origin main

一、报错原因
你的 GitHub 云端仓库 不是空的（比如有 README.md），
但你本地文件夹是空的 / 不一样，所以 Git 不让你直接推。
二、100% 能解决的命令（直接复制运行）
在你的 Git Bash 里依次输入这两行：
bash
运行
git pull origin main --allow-unrelated-histories
然后再推：
bash
运行
git push origin main



## 5. 后续上传最简固定流程（你本地是 master 分支）

bash运行

```
git add .
git commit -m "更新备注"
git push
```

bash运行

```
git remote -v
```

能看到 origin 对应的推送 / 拉取地址，证明绑定成功

1. 生成 SSH 密钥（用 Git Bash / Terminal / PowerShell）
  推荐用 ed25519（安全、短、快）：
  bash
  运行

  ```
  ssh-keygen -t ed25519 -C "你的GitHub注册邮箱"
  ```

  提示保存位置：直接回车（默认 ~/.ssh/id_ed25519）
  提示密码：可以留空（直接回车），也可以设密码（更安全）

一、最快解决方法（直接用 443 端口）打开 Git Bash，输入下面这行命令：bash运行

```
ssh -T -p 443 git@ssh.github.com
```

 看到提示输入 yes 回车。如果出现：plaintextHi HD-Zhong! You've successfully authenticated... ✅ 直接成功！二、永久修复（以后 git push 不再报错）在 Git Bash 里执行：bash运行

```
touch ~/.ssh/config notepad ~/.ssh/config
```

 在打开的记事本里粘贴下面全部内容：

plaintextHost github.com  

​	Hostname ssh.github.com  

​	Port 443  

​	User git  

​	IdentityFile ~/.ssh/id_ed25519

 保存关闭。

然后再测试：
bash
运行

```
ssh -T git@github.com
```

