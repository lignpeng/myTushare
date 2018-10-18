
var loader = new Object()
/**
16      * 加载外部的js文件
17      * @param sUrl 要加载的js的url地址
18      * @fCallback js加载完成之后的处理函数
19      */
loader.JsLoader={
  load:function(sUrl,callback){
    var _script=document.createElement('script');
    _script.setAttribute('charset','gbk');
    _script.setAttribute('type','text/javascript');
    _script.setAttribute('src',sUrl);
    document.getElementsByTagName('head')[0].appendChild(_script);
    if(callback != undefined){
      callback()
    }
  }
}
