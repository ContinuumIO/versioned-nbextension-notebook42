;(function(){
  var __version__ = "0.1.0",
    __name__ = "foo-tree";
  console.log(__name__, __version__, "Loaded");

  define(["base/js/namespace"], function(Jupyter){
    console.log(__name__, __version__, "Defined");
    
    return {
      load_ipython_extension: function(){
        console.log(__name__, __version__, "Enabled");
      }
    }
  });
}).call(this);
