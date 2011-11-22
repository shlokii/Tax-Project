var NAVTREE =
[
  [ "Tax-Project", "index.html", [
    [ "Class List", "annotated.html", [
      [ "online_payment::admin::AAdmin", "classonline__payment_1_1admin_1_1AAdmin.html", null ],
      [ "online_payment::models::Accounts_dummy", "classonline__payment_1_1models_1_1Accounts__dummy.html", null ],
      [ "online_payment::models::BackOffice_dummy", "classonline__payment_1_1models_1_1BackOffice__dummy.html", null ],
      [ "online_payment::admin::BOAdmin", "classonline__payment_1_1admin_1_1BOAdmin.html", null ],
      [ "online_payment::forms::ContactForm", "classonline__payment_1_1forms_1_1ContactForm.html", null ],
      [ "online_payment::models::Online_Transaction_dummy", "classonline__payment_1_1models_1_1Online__Transaction__dummy.html", null ],
      [ "online_payment::admin::OTAdmin", "classonline__payment_1_1admin_1_1OTAdmin.html", null ],
      [ "online_payment::tests::PrintTransaction", "classonline__payment_1_1tests_1_1PrintTransaction.html", null ],
      [ "online_payment::models::Service_Tax", "classonline__payment_1_1models_1_1Service__Tax.html", null ],
      [ "online_payment::admin::ServiceAdmin", "classonline__payment_1_1admin_1_1ServiceAdmin.html", null ],
      [ "online_payment::models::Tax_transaction", "classonline__payment_1_1models_1_1Tax__transaction.html", null ],
      [ "online_payment::admin::TaxAdmin", "classonline__payment_1_1admin_1_1TaxAdmin.html", null ],
      [ "online_payment::models::Taxtype", "classonline__payment_1_1models_1_1Taxtype.html", null ],
      [ "online_payment::admin::TTAdmin", "classonline__payment_1_1admin_1_1TTAdmin.html", null ]
    ] ],
    [ "Class Index", "classes.html", null ],
    [ "Class Members", "functions.html", null ],
    [ "Namespace List", "namespaces.html", [
      [ "online_payment", "namespaceonline__payment.html", null ],
      [ "online_payment::admin", "namespaceonline__payment_1_1admin.html", null ],
      [ "online_payment::forms", "namespaceonline__payment_1_1forms.html", null ],
      [ "online_payment::models", "namespaceonline__payment_1_1models.html", null ],
      [ "online_payment::tests", "namespaceonline__payment_1_1tests.html", null ],
      [ "online_payment::views", "namespaceonline__payment_1_1views.html", null ],
      [ "tax", "namespacetax.html", null ],
      [ "tax::settings", "namespacetax_1_1settings.html", null ],
      [ "tax::urls", "namespacetax_1_1urls.html", null ],
      [ "tax::urls1", "namespacetax_1_1urls1.html", null ]
    ] ],
    [ "Namespace Members", "namespacemembers.html", null ],
    [ "File List", "files.html", [
      [ "online_payment/__init__.py", "online__payment_2____init_____8py.html", null ],
      [ "online_payment/admin.py", "admin_8py.html", null ],
      [ "online_payment/forms.py", "forms_8py.html", null ],
      [ "online_payment/models.py", "models_8py.html", null ],
      [ "online_payment/tests.py", "tests_8py.html", null ],
      [ "online_payment/views.py", "views_8py.html", null ],
      [ "tax/__init__.py", "tax_2____init_____8py.html", null ],
      [ "tax/settings.py", "settings_8py.html", null ],
      [ "tax/urls.py", "urls_8py.html", null ],
      [ "tax/urls1.py", "urls1_8py.html", null ]
    ] ],
    [ "Directories", "dirs.html", [
      [ "online_payment", "dir_896d1335d0a7cbf326fa861f6c268fe3.html", [
        [ "__init__.py", "online__payment_2____init_____8py.html", null ],
        [ "admin.py", "admin_8py.html", null ],
        [ "forms.py", "forms_8py.html", null ],
        [ "models.py", "models_8py.html", null ],
        [ "tests.py", "tests_8py.html", null ],
        [ "views.py", "views_8py.html", null ]
      ] ],
      [ "tax", "dir_c13036086f6999bc7505097da36f494d.html", [
        [ "__init__.py", "tax_2____init_____8py.html", null ],
        [ "settings.py", "settings_8py.html", null ],
        [ "urls.py", "urls_8py.html", null ],
        [ "urls1.py", "urls1_8py.html", null ]
      ] ]
    ] ]
  ] ]
];

function createIndent(o,domNode,node,level)
{
  if (node.parentNode && node.parentNode.parentNode)
  {
    createIndent(o,domNode,node.parentNode,level+1);
  }
  var imgNode = document.createElement("img");
  if (level==0 && node.childrenData)
  {
    node.plus_img = imgNode;
    node.expandToggle = document.createElement("a");
    node.expandToggle.href = "javascript:void(0)";
    node.expandToggle.onclick = function() 
    {
      if (node.expanded) 
      {
        $(node.getChildrenUL()).slideUp("fast");
        if (node.isLast)
        {
          node.plus_img.src = node.relpath+"ftv2plastnode.png";
        }
        else
        {
          node.plus_img.src = node.relpath+"ftv2pnode.png";
        }
        node.expanded = false;
      } 
      else 
      {
        expandNode(o, node, false);
      }
    }
    node.expandToggle.appendChild(imgNode);
    domNode.appendChild(node.expandToggle);
  }
  else
  {
    domNode.appendChild(imgNode);
  }
  if (level==0)
  {
    if (node.isLast)
    {
      if (node.childrenData)
      {
        imgNode.src = node.relpath+"ftv2plastnode.png";
      }
      else
      {
        imgNode.src = node.relpath+"ftv2lastnode.png";
        domNode.appendChild(imgNode);
      }
    }
    else
    {
      if (node.childrenData)
      {
        imgNode.src = node.relpath+"ftv2pnode.png";
      }
      else
      {
        imgNode.src = node.relpath+"ftv2node.png";
        domNode.appendChild(imgNode);
      }
    }
  }
  else
  {
    if (node.isLast)
    {
      imgNode.src = node.relpath+"ftv2blank.png";
    }
    else
    {
      imgNode.src = node.relpath+"ftv2vertline.png";
    }
  }
  imgNode.border = "0";
}

function newNode(o, po, text, link, childrenData, lastNode)
{
  var node = new Object();
  node.children = Array();
  node.childrenData = childrenData;
  node.depth = po.depth + 1;
  node.relpath = po.relpath;
  node.isLast = lastNode;

  node.li = document.createElement("li");
  po.getChildrenUL().appendChild(node.li);
  node.parentNode = po;

  node.itemDiv = document.createElement("div");
  node.itemDiv.className = "item";

  node.labelSpan = document.createElement("span");
  node.labelSpan.className = "label";

  createIndent(o,node.itemDiv,node,0);
  node.itemDiv.appendChild(node.labelSpan);
  node.li.appendChild(node.itemDiv);

  var a = document.createElement("a");
  node.labelSpan.appendChild(a);
  node.label = document.createTextNode(text);
  a.appendChild(node.label);
  if (link) 
  {
    a.href = node.relpath+link;
  } 
  else 
  {
    if (childrenData != null) 
    {
      a.className = "nolink";
      a.href = "javascript:void(0)";
      a.onclick = node.expandToggle.onclick;
      node.expanded = false;
    }
  }

  node.childrenUL = null;
  node.getChildrenUL = function() 
  {
    if (!node.childrenUL) 
    {
      node.childrenUL = document.createElement("ul");
      node.childrenUL.className = "children_ul";
      node.childrenUL.style.display = "none";
      node.li.appendChild(node.childrenUL);
    }
    return node.childrenUL;
  };

  return node;
}

function showRoot()
{
  var headerHeight = $("#top").height();
  var footerHeight = $("#nav-path").height();
  var windowHeight = $(window).height() - headerHeight - footerHeight;
  navtree.scrollTo('#selected',0,{offset:-windowHeight/2});
}

function expandNode(o, node, imm)
{
  if (node.childrenData && !node.expanded) 
  {
    if (!node.childrenVisited) 
    {
      getNode(o, node);
    }
    if (imm)
    {
      $(node.getChildrenUL()).show();
    } 
    else 
    {
      $(node.getChildrenUL()).slideDown("fast",showRoot);
    }
    if (node.isLast)
    {
      node.plus_img.src = node.relpath+"ftv2mlastnode.png";
    }
    else
    {
      node.plus_img.src = node.relpath+"ftv2mnode.png";
    }
    node.expanded = true;
  }
}

function getNode(o, po)
{
  po.childrenVisited = true;
  var l = po.childrenData.length-1;
  for (var i in po.childrenData) 
  {
    var nodeData = po.childrenData[i];
    po.children[i] = newNode(o, po, nodeData[0], nodeData[1], nodeData[2],
        i==l);
  }
}

function findNavTreePage(url, data)
{
  var nodes = data;
  var result = null;
  for (var i in nodes) 
  {
    var d = nodes[i];
    if (d[1] == url) 
    {
      return new Array(i);
    }
    else if (d[2] != null) // array of children
    {
      result = findNavTreePage(url, d[2]);
      if (result != null) 
      {
        return (new Array(i).concat(result));
      }
    }
  }
  return null;
}

function initNavTree(toroot,relpath)
{
  var o = new Object();
  o.toroot = toroot;
  o.node = new Object();
  o.node.li = document.getElementById("nav-tree-contents");
  o.node.childrenData = NAVTREE;
  o.node.children = new Array();
  o.node.childrenUL = document.createElement("ul");
  o.node.getChildrenUL = function() { return o.node.childrenUL; };
  o.node.li.appendChild(o.node.childrenUL);
  o.node.depth = 0;
  o.node.relpath = relpath;

  getNode(o, o.node);

  o.breadcrumbs = findNavTreePage(toroot, NAVTREE);
  if (o.breadcrumbs == null)
  {
    o.breadcrumbs = findNavTreePage("index.html",NAVTREE);
  }
  if (o.breadcrumbs != null && o.breadcrumbs.length>0)
  {
    var p = o.node;
    for (var i in o.breadcrumbs) 
    {
      var j = o.breadcrumbs[i];
      p = p.children[j];
      expandNode(o,p,true);
    }
    p.itemDiv.className = p.itemDiv.className + " selected";
    p.itemDiv.id = "selected";
    $(window).load(showRoot);
  }
}

