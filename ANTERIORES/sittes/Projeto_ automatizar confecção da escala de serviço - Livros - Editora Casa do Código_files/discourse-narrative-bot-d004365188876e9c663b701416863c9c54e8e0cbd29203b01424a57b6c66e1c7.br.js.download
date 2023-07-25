define("discourse/plugins/discourse-narrative-bot/initializers/new-user-narrative",["exports","discourse/lib/plugin-api","discourse-common/utils/decorators"],(function(e,i,t){"use strict"
var r
Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0
var s,a,n,o,u,c,l=(s=r={name:"new-user-narrative",initialize(e){e.lookup("service:site-settings").discourse_narrative_bot_enabled&&(this.messageBus=e.lookup("service:message-bus"),this.appEvents=e.lookup("service:app-events"),(0,i.withPluginApi)("0.8.7",(e=>{this.currentUser=e.getCurrentUser(),this.currentUser&&(e.dispatchWidgetAppEvent("site-header","header","header:search-context-trigger"),e.attachWidgetAction("header","headerSearchContextTrigger",(function(){this.site.mobileView?this.state.skipSearchContext=!1:(this.state.contextEnabled=!0,this.state.searchContextType="topic")})),this.messageBus.subscribe(`/new_user_narrative/tutorial_search/${this.currentUser.id}`,this.onMessage))})))},teardown(){this.currentUser&&this.messageBus?.unsubscribe(`/new_user_narrative/tutorial_search/${this.currentUser.id}`,this.onMessage)},onMessage(){this.appEvents.trigger("header:search-context-trigger")}},a="onMessage",n=[t.bind],o=Object.getOwnPropertyDescriptor(r,"onMessage"),u=r,c={},Object.keys(o).forEach((function(e){c[e]=o[e]})),c.enumerable=!!c.enumerable,c.configurable=!!c.configurable,("value"in c||c.initializer)&&(c.writable=!0),c=n.slice().reverse().reduce((function(e,i){return i(s,a,e)||e}),c),u&&void 0!==c.initializer&&(c.value=c.initializer?c.initializer.call(u):void 0,c.initializer=void 0),void 0===c.initializer&&(Object.defineProperty(s,a,c),c=null),r)
e.default=l}))

//# sourceMappingURL=discourse-narrative-bot-16492afed6474e0cee7faea44ffd3158cc9fa7df0961935894d4beb6446fb2be.map
//!

;
