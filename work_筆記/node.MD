# JS 結構 of 貓博士 研發測試版本
[TOC]
## backend
因為這邊是使用 AWS 
### SRC
#### lambda
**function file**
:::success
db change condition
```
index.ts
```
路徑設定
```
config設定
```
:::
##### migration
back up
:::success
db相關設定
```
index.js
```
副本標記
```
table.js
```
路徑設定
```
config.json
```
:::

#### share ORM of node.js
:::success
(帳號設定)
```
gen.ts
```
(db設定)
```
db.ts
```
(aws db的path 等設定)
```
uril.ts
```
:::
#### taken
### STACK
:::success
yml(api)
1. 把api 設定好後
   就manu get the gateway of server
2. db 設訂定
3. 函數設定
**yaml如果上aws的檔案名不一樣**
4. 前端api
5. server api
:::
### root
package-lock.json
:::info
hint:官方版本
package-lock.json的作用就是鎖定安裝依賴時包的版本，並且需要上傳到git，以保證其他人npm install時安裝的依賴能夠保持一致

根據官方文檔，這個package-lock.json 是在 `npm install`時候生成的一份文件，用以記錄當前狀態下實際安裝的各個npm package的具體來源和版本號。
:::
package.json
:::success
hint:自己管理版本
因為npm是一個用於管理package之間依賴關系的管理器，它允許開發者在pacakge.json中間標出自己項目對npm各庫包的依賴。你可以選擇以如下方式來標明自己所需要庫包的版本
:::
tsconfing.json
:::success
1. target： 輸出的JavaScript版本(可選 ES3、 ES5 、 ES2015 、 ES2016 、 ES2017 、 ES2018 、 ESNext 和 JSON)
2. JSX： 是否使用JSX語法
3. Lang: 切換支援 TS 和 JS 語法
``` =bash
tsc --init
```
:::
:::info
``` =json
{
    "compilerOptions": {
        "target": "es5",  //指定編譯生成的JS版本
        "module": "commonjs", //指定生成哪種模組
        "strict": true,  //採用嚴格模式  
        "esModuleInterop": true,  //兼容模組導入的方式
    }
}
```
:::
tslint.json
:::success
變數定義
:::
webpack.config.js
:::success
猶如齊名是
這邊是設定 api 等路徑
:::
```

```
## frontend (angular) mode
### e2e 
End to End
### provision
backup time log
### shared orm 自訂庫

### src main app 研發區

### root 
跟前面的root 設定差不多
