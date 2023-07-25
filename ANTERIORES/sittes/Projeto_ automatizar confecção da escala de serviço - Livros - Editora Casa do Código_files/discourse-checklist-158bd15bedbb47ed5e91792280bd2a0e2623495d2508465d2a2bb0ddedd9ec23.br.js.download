define("discourse/plugins/discourse-checklist/discourse/initializers/checklist",["exports","discourse/lib/plugin-api","discourse/lib/ajax","discourse-common/lib/icon-library","I18n"],(function(e,n,t,c,s){"use strict"
function i(e){e.forEach((e=>e.classList.remove("readonly")))}function a(e){return 3===e.nodeType&&e.nodeValue.match(/^\s*$/)}function o(e){e.forEach((e=>{let n=e.parentElement
"P"===n.nodeName&&n.parentElement.firstElementChild===n&&(n=n.parentElement),"LI"===n.nodeName&&"UL"===n.parentElement.nodeName&&(function(e){let n=e.previousSibling
for(;n;){if(!a(n))return!0
n=n.previousSibling}return!1}(e)||(n.classList.add("has-checkbox"),e.classList.add("list-item-checkbox"),e.nextSibling||e.insertAdjacentHTML("afterend","&#8203;")))}))}function r(e,n){const a=[...e.getElementsByClassName("chcklst-box")]
if(o(a),!n)return
const r=n.widget,l=n.getModel()
l.can_edit&&a.forEach(((e,n)=>{e.onclick=function(e){const o=e.currentTarget,d=o.classList
if(d.contains("permanent")||d.contains("readonly"))return
const u=d.contains("checked")?"[ ]":"[x]",f=document.createElement("template")
f.innerHTML=(0,c.iconHTML)("spinner",{class:"fa-spin"}),o.insertAdjacentElement("afterend",f.content.firstChild),o.classList.add("hidden"),a.forEach((e=>e.classList.add("readonly"))),(0,t.ajax)(`/posts/${l.id}`,{type:"GET",cache:!1}).then((e=>{const t=[];[/`[^`\n]*\n?[^`\n]*`/gm,/^```[^]*?^```/gm,/\[code\][^]*?\[\/code\]/gm,/_(?=\S).*?\S_/gm,/~~(?=\S).*?\S~~/gm].forEach((n=>{let c
for(;null!=(c=n.exec(e.raw));)t.push([c.index,c.index+c[0].length])})),[/([^\[\n]|^)\*\S.+?\S\*(?=[^\]\n]|$)/gm].forEach((n=>{let c
for(;null!=(c=n.exec(e.raw));)t.push([c.index+1,c.index+c[0].length])}))
let c=-1,o=!1
const d=e.raw.replace(/\[(\s|\_|\-|\x|\\?\*)?\]/gi,((e,s,i)=>o?e:(c+=t.every((n=>n[0]>=i+e.length||i>n[1])),c===n?(o=!0,u):e))),f=l.save({raw:d,edit_reason:s.default.t("checklist.edit_reason")})
f&&f.then?f.then((()=>{r.attrs.isSaving=!1,r.scheduleRerender()})).finally((()=>i(a))):i(a)})).catch((()=>i(a)))}}))}Object.defineProperty(e,"__esModule",{value:!0}),e.checklistSyntax=r,e.default=void 0
var l={name:"checklist",initialize:function(){(0,n.withPluginApi)("0.1",(e=>function(e){e.container.lookup("site-settings:main").checklist_enabled&&e.decorateCookedElement(r,{id:"checklist"})}(e)))}}
e.default=l})),define("discourse/plugins/discourse-checklist/lib/discourse-markdown/checklist",["exports"],(function(e){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.setup=function(e){e.registerOptions(((e,n)=>{e.features.checklist=!!n.checklist_enabled})),e.allowList(["span.chcklst-stroked","span.chcklst-box fa fa-square-o fa-fw","span.chcklst-box checked fa fa-check-square-o fa-fw","span.chcklst-box checked permanent fa fa-check-square fa-fw"]),e.registerPlugin((e=>e.core.ruler.push("checklist",s)))}
const n=/\[(\s?|x|X)\]/g
function t(e,n,t,c){const s=function(e){switch(e){case"x":return"checked fa fa-check-square-o fa-fw"
case"X":return"checked permanent fa fa-check-square fa-fw"
default:return"fa fa-square-o fa-fw"}}(t[1]),i=new c.Token("check_open","span",1)
i.attrs=[["class",`chcklst-box ${s}`]],e.push(i)
const a=new c.Token("check_close","span",-1)
e.push(a)}function c(e,c){let s,i=null,a=0
for(;s=n.exec(e);){if(s.index>a){i=i||[]
const n=new c.Token("text","",0)
n.content=e.slice(a,s.index),i.push(n)}a=s.index+s[0].length,i=i||[],t(i,0,s,c)}if(i&&a<e.length){const n=new c.Token("text","",0)
n.content=e.slice(a),i.push(n)}return i}function s(e){let n,t,s,i,a,o=e.tokens,r=0
for(t=0,s=o.length;t<s;t++)if("inline"===o[t].type)for(i=o[t].children,n=i.length-1;n>=0;n--)if(a=i[n],r+=a.nesting,"text"===a.type&&0===r){const s=c(a.content,e)
s&&(o[t].children=i=e.md.utils.arrayReplaceAt(i,n,s))}}}))

//# sourceMappingURL=discourse-checklist-f1c5dba8e478a5705791ea2ba949e80517d865e6524e978d360837de89422452.map
//!

;
