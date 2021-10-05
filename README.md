# Feedly to LinkAce _(feedly-to-linkace)_

> Feedly記事をLinkAceブックマークに自動登録する

## Install

Dockerを使用します。

```
$ docker version
Client: Docker Engine - Community
 Version:           20.10.8
 API version:       1.41
 Go version:        go1.16.6
 Git commit:        3967b7d
 Built:             Fri Jul 30 19:54:27 2021
 OS/Arch:           linux/amd64
 Context:           default
 Experimental:      true

Server: Docker Engine - Community
 Engine:
  Version:          20.10.8
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.16.6
  Git commit:       75249d8
  Built:            Fri Jul 30 19:52:33 2021
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.4.9
  GitCommit:        e25210fe30a0a703442421b0f60afac609f950a3
 runc:
  Version:          1.0.1
  GitCommit:        v1.0.1-0-g4144b63
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```

## Usage

```
$ docker run --rm ghcr.io/u6k/feedly-to-linkace pipenv run main
```

## Other

最新の情報は、[Wiki - bookmark - u6k.Redmine](https://redmine.u6k.me/projects/bookmark-bundler/wiki/Wiki)を参照してください。

### リリース手順

- リリース・ブランチを開始する
- TODOコメントを確認する
- バージョンを更新する
    - `.github/workflows/build-and-push.yml`
    - `feedly_to_linkace/__init__.py`
- CHANGELOGを最新化する
- CIの成功を確認する
- リリース・ブランチを終了する
- バージョンを更新して`-develop`サフィックスを追加する
- GitHubリリース・ノートを編集する

## Maintainer

- u6k
    - [Twitter](https://twitter.com/u6k_yu1)
    - [GitHub](https://github.com/u6k)
    - [Blog](https://blog.u6k.me/)

## Contributing

当プロジェクトに興味を持っていただき、ありがとうございます。[既存のチケット](https://redmine.u6k.me/projects/bookmark-bundler/issues/)をご覧ください。

当プロジェクトは、[Contributor Covenant](https://www.contributor-covenant.org/version/1/4/code-of-conduct)に準拠します。

## License

[MIT License](https://github.com/u6k/feedly-to-linkace/blob/master/LICENSE)
