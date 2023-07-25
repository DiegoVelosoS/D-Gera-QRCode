define("discourse/plugins/discourse-details/initializers/apply-details",["exports","I18n","discourse/lib/plugin-api"],(function(e,i,t){"use strict"
function s(e){e.decorateCooked((e=>$("details",e)),{id:"discourse-details"}),e.addToolbarPopupMenuOptionsCallback((()=>({action:"insertDetails",icon:"caret-right",label:"details.title"}))),e.modifyClass("controller:composer",{pluginId:"discourse-details",actions:{insertDetails(){this.toolbarEvent.applySurround(`\n[details="${i.default.t("composer.details_title")}"]\n`,"\n[/details]\n","details_text",{multiline:!1})}}})}Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
var l={name:"apply-details",initialize(){(0,t.withPluginApi)("0.8.7",s)}}
e.default=l})),define("discourse/plugins/discourse-details/lib/discourse-markdown/details",["exports"],(function(e){"use strict"
Object.defineProperty(e,"__esModule",{value:!0}),e.setup=function(e){e.allowList(["summary","summary[title]","details","details[open]","details.elided"]),e.registerPlugin((e=>{e.block.bbcode.ruler.push("details",i)}))}
const i={tag:"details",before(e,i){const t=i.attrs
e.push("bbcode_open","details",1),e.push("bbcode_open","summary",1),e.push("text","",0).content=t._default||"",e.push("bbcode_close","summary",-1)},after(e){e.push("bbcode_close","details",-1)}}}))

//# sourceMappingURL=discourse-details-bdd32663c925488d09ccddb6747329faac7507f5dfcc8dbdf6b455912c44b559.map
//!

;
