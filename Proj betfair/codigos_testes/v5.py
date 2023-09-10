from bs4 import BeautifulSoup
import pandas as pd
tabela  = """<bf-marketview-header-wrapper market-id="miniMvCtrl.viewModel.marketId" market-name="miniMvCtrl.viewModel.market.name" event-type-id="miniMvCtrl.viewModel.market.eventTypeId" market-type="miniMvCtrl.viewModel.market.marketType" country-code="miniMvCtrl.viewModel.market.countryCode" is-closed="miniMvCtrl.viewModel.market.isClosed" inplay="miniMvCtrl.viewModel.market.inplay" in-play-enabled="miniMvCtrl.viewModel.market.inPlayEnabled" is-place-or-win="miniMvCtrl.viewModel.market.isPlaceOrWin" should-show-bsp="miniMvCtrl.viewModel.market.shouldShowBSP" is-ah="miniMvCtrl.viewModel.market.isAH" is-ah-double-line="miniMvCtrl.viewModel.market.isAHDoubleLine" is-over-asian-handicap-active-runners-limit="miniMvCtrl.viewModel.market.isOverAsianHandicapActiveRunnersLimit" theme="mini-marketview" gtm-module="miniMvCtrl.viewModel.gtmModule"><div class="marketview-header-wrapper-container bf-col-24-24"><div class="marketview-header-wrapper-bottom-container new-theme" ng-class="{      
            closed:
                ctrl.vm.data.market.isClosed,
            'has-favourites':
                ctrl.vm.data.hasFavourites,
            'new-theme': ctrl.vm.data.shouldUseNewTheme
         }"><!----><!----><marketview-header data="ctrl.vm.data"><div class="mv-header-container mini-marketview" ng-class="ctrl.data.marketHeaderTheme"><div class="mv-header-content"><div class="mv-header-main-section-wrapper"><!----><div class="market-name" ng-if="ctrl.data.marketHeaderTheme === 'mini-marketview' &amp;&amp; 
ctrl.data.marketNameSettings.visible"><span class="market-name-label" ng-bind="ctrl.data.marketNameSettings.label">Mais/Menos de 3,5 Gols</span></div><!----><div class="mv-header-main-section"><!----><div class="market-status mv-header-field market-inplay" ng-class="ctrl.data.marketStatus.class" ng-if="ctrl.data.marketStatus.visible"><span class="market-status-icon"></span> <!----></div><!----><!----><div class="cashout-availability mv-header-field" ng-if="ctrl.data.cashout.visible" ng-attr-title="{{::ctrl.data.cashout.tooltip}}" title="Cash out disponível neste mercado"><span class="cashout-icon"></span> <!----></div><!----><!----><span class="market-rules mv-header-field" ng-if="ctrl.data.marketRules.visible"><a class="market-rules-link" ng-click="ctrl.data.marketRules.onClick()"><span class="market-rules-icon"></span> <!----><span class="market-rules-label" ng-if="ctrl.data.marketRules.label" ng-bind="::ctrl.data.marketRules.label">Regras</span><!----></a></span><!----><!----><!----><!----><!----><!----></div></div><!----></div></div></marketview-header><div class="modal-dialog ng-hide" ng-show="show" show="ctrl.vm.data.contextualHelpPopup.show" width="300px"><div class="overlay" ng-click="hideDialog();"><div class="dialog-container"><div class="dialog" ng-style="dialogStyle" ng-click="$event.stopPropagation();" style="width: 300px;"><div class="dialog-header"><span class="dialog-title" ng-bind="modalDialogTitle"></span> <span class="close-dialog" ng-click="hideDialog()"></span></div><section class="dialog-content" ng-transclude=""><div class="sp-tooltip-text"><p ng-bind-template="Você pode optar por mostrar cotações ao Preço inicial Betfair (PIB). As apostas feitas com o preço inicial são liquidadas ao Preço inicial Betfair (PIB). Apostas ao Preço inicial Betfair (PIB) 
não podem ser canceladas quando feitas.">Você pode optar por mostrar cotações ao Preço inicial Betfair (PIB). As apostas feitas com o preço inicial são liquidadas ao Preço inicial Betfair (PIB). Apostas ao Preço inicial Betfair (PIB) não podem ser canceladas quando feitas.</p><p><a href="https://en-betfair.custhelp.com/app/answers/detail/a_id/421" ng-bind-template="Consulte a ajuda Preço inicial Betfair (PIB) para saber mais." target="_blank">Consulte a ajuda Preço inicial Betfair (PIB) 
para saber mais.</a></p></div></section></div></div></div></div></div><!----></div></bf-marketview-header-wrapper><!----><bf-cashout-wrapper market-id="miniMvCtrl.viewModel.marketId" event-type-id="miniMvCtrl.viewModel.market.eventTypeId" ga-module="miniMvCtrl.viewModel.gtmModule" bf-throttle="'cashout'"><!----></bf-cashout-wrapper><!-- end bfThrottle: 'cashout' --><!----><bf-runners-header ng-if="!miniMvCtrl.viewModel.isCollapsed" total-matched="miniMvCtrl.viewModel.market.totalMatched" is-closed="miniMvCtrl.viewModel.market.isClosed" back-label="A favor" lay-label="Contra"><table class="runners-header"><thead><tr class="rh-line" ng-class="{'without-lay': !rhCtrl.layLabel}"><th class="rh-runner-name-header"><!----><span class="rh-matched-amount-label" ng-if="rhCtrl.vm.data.marketMatched.visible" ng-bind-template="Correspondido: BRL 299,378">Correspondido: BRL 299,378</span><!----> <!----> <!----></th><!----><!----><!----><th ng-if="rhCtrl.backLabel" ng-class="{'is-small': !rhCtrl.displayMarketDepth}" class="rh-label-all is-small"><span class="rh-label-back" ng-bind-template="A favor">A favor</span></th><!----><!----><!----><!----><th ng-if="rhCtrl.layLabel" ng-class="{'is-small': !rhCtrl.displayMarketDepth}" class="rh-label-all is-small"><span class="rh-label-lay" ng-bind-template="Contra">Contra</span></th><!----><!----></tr></thead></table></bf-runners-header><!----><!----><div ng-if="!miniMvCtrl.viewModel.isCollapsed" class="mini-mv-runners-list-wrapper" suspended-overlay="miniMvCtrl.viewModel.market.isSuspended"><bf-marketview-runners-list is-bsp-reconciled="miniMvCtrl.viewModel.market.bspReconciled" country-code="miniMvCtrl.viewModel.market.countryCode" event-type-id="miniMvCtrl.viewModel.market.eventTypeId" has-pnl-inline="miniMvCtrl.viewModel.market.hasPnlInline" market-id="miniMvCtrl.viewModel.marketId" is-ah-double-line="miniMvCtrl.viewModel.market.isAHDoubleLine" is-closed="miniMvCtrl.viewModel.market.isClosed" is-hr="miniMvCtrl.viewModel.market.isHR" is-gh="miniMvCtrl.viewModel.market.isGH" is-place-or-win="miniMvCtrl.viewModel.market.isPlaceOrWin" is-saddlecloth-racing="miniMvCtrl.viewModel.market.isSaddleclothRacing" is-suspended="miniMvCtrl.viewModel.market.isSuspended" inplay="miniMvCtrl.viewModel.market.inplay" market-type="miniMvCtrl.viewModel.market.marketType" display-lay-prices="miniMvCtrl.viewModel.preferences.displayLayPrices" display-profit-and-loss="miniMvCtrl.viewModel.preferences.displayProfitAndLoss" display-future-profit-and-loss="miniMvCtrl.viewModel.preferences.displayFutureProfitAndLoss" enable-flashing-update-buttons="miniMvCtrl.viewModel.preferences.flashingUpdateButtonsEnabled" show-fractional-odds="miniMvCtrl.viewModel.preferences.showFractionalOdds" display-market-depth="::miniMvCtrl.viewModel.preferences.displayMarketDepth" display-race-card-info="::miniMvCtrl.viewModel.preferences.displayRaceCardInfo" display-sp-bets="::miniMvCtrl.viewModel.preferences.displaySPBets" display-sp-bets-near-far="::miniMvCtrl.viewModel.preferences.displaySPBetsNearFar" display-sp-bets-none="::miniMvCtrl.viewModel.preferences.displaySPBetsNone" display-sp-bets-projected-odds="::miniMvCtrl.viewModel.preferences.displaySPBetsProjectedOdds" display-timeform123="false" runners="miniMvCtrl.viewModel.runners" 
pnl="miniMvCtrl.viewModel.pnl" on-add-bet="miniMvCtrl.actions.addBet(betType, price, runner)" inline-betting-state="miniMvCtrl.viewModel.inlineBettingState"><div class="marketview-list-runners-component bf-row"><div class="runners-container bf-col-24-24"><div class="mv-runner-list-container overlayPosition"><bf-overlay ng-show="ctrl.vm.data.settings.overlayCashOutMessage" elem="'.mv-runner-list-container'" class="bf-overlay runner-list-overlay ng-hide"></bf-overlay><table class="mv-runner-list fixed-size" ng-class="{
                       'aus-greyhounds': ctrl.vm.data.isAusGreyhounds,
                       'fixed-size': !ctrl.vm.data.prefs.displayMarketDepth,
                       'market-closed': ctrl.vm.data.market.isClosed,
                       'small': ctrl.vm.data.isSmallTable,
                       'large': ctrl.vm.data.isLargeTable
                   }"><tbody><!----><tr class="runner-line" ng-repeat-start="runner in ctrl.vm.data.runners | filter:{isVisibleOnMarket:true} track by runner.key" ng-class="{
                        'loser-runner': runner.isLoser,
                        'removed-runner': runner.isRemoved || runner.isRemovedVacant,
                        'winner-runner': runner.isWinner || runner.isPlaced
                    }"><!----><td class="new-runner-info" ng-class="{
                            'with-pin-runners': ctrl.pinRunnersEditMode,
                            'without-lay': !ctrl.vm.data.prefs.displayLayPrices,
                            'with-runner-timeform-info': ctrl.vm.data.prefs.displayTimeform123 &amp;&amp; runner.isActive &amp;&amp; ctrl.vm.data.timeformRunners[runner.selectionId]
                        }" colspan="" ng-click="::ctrl.vm.events.runnerInfoDropdownClick(runner.selectionId, runner.isActive)"><!----><!----><div class="runner-info-container"><div class="market-graph-container"><!----><bf-market-graph market-id="::ctrl.vm.data.market.id" selection-id="::runner.selectionId" handicap="::runner.handicap" ng-click="ctrl.vm.events.handleOpenedGraphGTM($event);" ng-if="runner.isActive &amp;&amp; ctrl.vm.data.market.eventTypeId" on-graph-window-closed="ctrl.vm.events.handleGraphWindowClosed();"><button class="market-graph" ng-click="ctrl.vm.events.openMarketGraph()"></button></bf-market-graph><!----></div><div class="runner-data-container without-race-card-info" ng-class="{
                                    'with-pnl': ctrl.vm.events.shouldShowPnl(runner),
                                    'without-race-card-info': !ctrl.vm.data.displayRaceCardInfo
                                 }"><bf-runner-info ng-class="ctrl.vm.data.market.isSaddleclothRacing ? 'name-saddlecloth' : 'name-silk'" type="default" runner="::runner" metadata="ctrl.vm.data.runnerMetadataMap[runner.selectionId]" show-race-card="ctrl.vm.data.displayRaceCardInfo" is-saddle-cloth-racing="ctrl.vm.data.market.isSaddleclothRacing" class="name-silk"><div ng-switch="::$ctrl.type" class="runner-info"><!----><!----><!----><div ng-switch-default="" class="default name"><h3 class="runner-name" ng-bind="$ctrl.runnerName">Menos de 3,5 gols</h3></div><!----></div></bf-runner-info></div><!----></div></td><!----><!----><!----><!----><!----><!----><td class="bet-buttons back-cell last-back-cell" ng-repeat="back in runner.toBack track by $index" ng-if="runner.isActive &amp;&amp; (ctrl.vm.data.prefs.displayMarketDepth || $last)" ng-class="{
                            'last-back-cell': $last,
                            'suspended': ctrl.vm.data.market.isSuspended,
                            'without-lay': !ctrl.vm.data.prefs.displayLayPrices
                        }" bet-type="back" bet-is-sp="false" bet-handicap="0" bet-selection-id="1222344"><ours-price-button type="back" price="ctrl.vm.events.getBetPrice(back.price)" size="ctrl.vm.events.getBetSize(back.size, !$last)" depth="runner.toBack.length - $index - 1" pressed="$last &amp;&amp; runner.isBackSelected" highlightable="ctrl.vm.data.prefs.flashingUpdateButtonsEnabled" hover-text="ctrl.vm.events.getBetButtonFractionalOdd(back)" disabled="ctrl.vm.data.market.isSuspended" on-click="ctrl.vm.events.addBet(ctrl.vm.data.betsConfiguration.types.back, back.price, runner)">
            <button class="_5iIjZ back FfpPi" ng-click="$ctrl.onClick()" ng-disabled="$ctrl.disabled" ng-attr-title="{{$ctrl.hoverText}}" ng-attr-is-best-selection="{{$ctrl.depth === 0}}" ng-attr-is-sp="{{$ctrl.isSp}}" ng-class="[
                    $ctrl.type,
                    {
                        'FfpPi': $ctrl.type === 'back',
                        '_4kgZU': $ctrl.type === 'lay',
                        'Sm8Nv': $ctrl.type === 'over',
                        'p0Mw+': $ctrl.type === 'under',
                        'SPkh1': $ctrl.pressed,
                        'd5UZ9': $ctrl.highlighted,
                        'bCGFk': $ctrl.depth
                    }
                ]" ng-attr-is-pressed="{{$ctrl.pressed}}" title="1/100" is-best-selection="true" is-pressed="false">
                <!---->
                <!----><label ng-if="!$ctrl.isSp" class="Zs3u5 AUP11 Qe-26">1.01</label><!---->
                <!----><label ng-if="!$ctrl.isSp" class="He6+y Qe-26">R$4571</label><!---->
            </button>
            </ours-price-button></td><!----><!----><!----><!----><!----><!----><!----><td class="bet-buttons lay-cell first-lay-cell" ng-repeat="lay in runner.toLay track by $index" ng-if="ctrl.vm.data.prefs.displayLayPrices &amp;&amp; runner.isActive &amp;&amp; (ctrl.vm.data.prefs.displayMarketDepth || $first)" ng-class="{   
                            'first-lay-cell': $first,
                            'suspended': ctrl.vm.data.market.isSuspended
                        }" bet-type="lay" bet-handicap="0" bet-selection-id="1222344"><ours-price-button type="lay" price="ctrl.vm.events.getBetPrice(lay.price)" size="ctrl.vm.events.getBetSize(lay.size, !$first)" depth="$index" pressed="$first &amp;&amp; runner.isLaySelected" highlightable="ctrl.vm.data.prefs.flashingUpdateButtonsEnabled" hover-text="ctrl.vm.events.getBetButtonFractionalOdd(lay)" disabled="ctrl.vm.data.market.isSuspended" on-click="ctrl.vm.events.addBet(ctrl.vm.data.betsConfiguration.types.lay, lay.price, runner)">
            <button class="_5iIjZ lay _4kgZU" ng-click="$ctrl.onClick()" ng-disabled="$ctrl.disabled" ng-attr-title="{{$ctrl.hoverText}}" ng-attr-is-best-selection="{{$ctrl.depth === 0}}" ng-attr-is-sp="{{$ctrl.isSp}}" ng-class="[
                    $ctrl.type,
                    {
                        'FfpPi': $ctrl.type === 'back',
                        '_4kgZU': $ctrl.type === 'lay',
                        'Sm8Nv': $ctrl.type === 'over',
                        'p0Mw+': $ctrl.type === 'under',
                        'SPkh1': $ctrl.pressed,
                        'd5UZ9': $ctrl.highlighted,
                        'bCGFk': $ctrl.depth
                    }
                ]" ng-attr-is-pressed="{{$ctrl.pressed}}" title="1/50" is-best-selection="true" is-pressed="false">
                <!---->
                <!----><label ng-if="!$ctrl.isSp" class="Zs3u5 AUP11 Qe-26">1.02</label><!---->
                <!----><label ng-if="!$ctrl.isSp" class="He6+y Qe-26">R$6497</label><!---->
            </button>
            </ours-price-button></td><!----><!----><!----><!----><!----><!----></tr><!----><!----><!----><tr class="runner-line" ng-repeat-start="runner in ctrl.vm.data.runners | filter:{isVisibleOnMarket:true} track by runner.key" ng-class="{
                        'loser-runner': runner.isLoser,
                        'removed-runner': runner.isRemoved || runner.isRemovedVacant,
                        'winner-runner': runner.isWinner || runner.isPlaced
                    }"><!----><td class="new-runner-info" ng-class="{
                            'with-pin-runners': ctrl.pinRunnersEditMode,
                            'without-lay': !ctrl.vm.data.prefs.displayLayPrices,
                            'with-runner-timeform-info': ctrl.vm.data.prefs.displayTimeform123 &amp;&amp; runner.isActive &amp;&amp; ctrl.vm.data.timeformRunners[runner.selectionId]
                        }" colspan="" ng-click="::ctrl.vm.events.runnerInfoDropdownClick(runner.selectionId, runner.isActive)"><!----><!----><div class="runner-info-container"><div class="market-graph-container"><!----><bf-market-graph market-id="::ctrl.vm.data.market.id" selection-id="::runner.selectionId" handicap="::runner.handicap" ng-click="ctrl.vm.events.handleOpenedGraphGTM($event);" ng-if="runner.isActive &amp;&amp; ctrl.vm.data.market.eventTypeId" on-graph-window-closed="ctrl.vm.events.handleGraphWindowClosed();"><button class="market-graph" ng-click="ctrl.vm.events.openMarketGraph()"></button></bf-market-graph><!----></div><div class="runner-data-container without-race-card-info" ng-class="{
                                    'with-pnl': ctrl.vm.events.shouldShowPnl(runner),
                                    'without-race-card-info': !ctrl.vm.data.displayRaceCardInfo
                                 }"><bf-runner-info ng-class="ctrl.vm.data.market.isSaddleclothRacing ? 'name-saddlecloth' : 'name-silk'" type="default" runner="::runner" metadata="ctrl.vm.data.runnerMetadataMap[runner.selectionId]" show-race-card="ctrl.vm.data.displayRaceCardInfo" is-saddle-cloth-racing="ctrl.vm.data.market.isSaddleclothRacing" class="name-silk"><div ng-switch="::$ctrl.type" class="runner-info"><!----><!----><!----><div ng-switch-default="" class="default name"><h3 class="runner-name" ng-bind="$ctrl.runnerName">Mais de 3,5 gols</h3></div><!----></div></bf-runner-info></div><!----></div></td><!----><!----><!----><!----><!----><!----><td class="bet-buttons back-cell last-back-cell" ng-repeat="back in runner.toBack track by $index" ng-if="runner.isActive &amp;&amp; (ctrl.vm.data.prefs.displayMarketDepth || $last)" ng-class="{
                            'last-back-cell': $last,
                            'suspended': ctrl.vm.data.market.isSuspended,
                            'without-lay': !ctrl.vm.data.prefs.displayLayPrices
                        }" bet-type="back" bet-is-sp="false" bet-handicap="0" bet-selection-id="1222345"><ours-price-button type="back" price="ctrl.vm.events.getBetPrice(back.price)" size="ctrl.vm.events.getBetSize(back.size, !$last)" depth="runner.toBack.length - $index - 1" pressed="$last &amp;&amp; runner.isBackSelected" highlightable="ctrl.vm.data.prefs.flashingUpdateButtonsEnabled" hover-text="ctrl.vm.events.getBetButtonFractionalOdd(back)" disabled="ctrl.vm.data.market.isSuspended" on-click="ctrl.vm.events.addBet(ctrl.vm.data.betsConfiguration.types.back, back.price, runner)">
            <button class="_5iIjZ back FfpPi" ng-click="$ctrl.onClick()" ng-disabled="$ctrl.disabled" ng-attr-title="{{$ctrl.hoverText}}" ng-attr-is-best-selection="{{$ctrl.depth === 0}}" ng-attr-is-sp="{{$ctrl.isSp}}" ng-class="[
                    $ctrl.type,
                    {
                        'FfpPi': $ctrl.type === 'back',
                        '_4kgZU': $ctrl.type === 'lay',
                        'Sm8Nv': $ctrl.type === 'over',
                        'p0Mw+': $ctrl.type === 'under',
                        'SPkh1': $ctrl.pressed,
                        'd5UZ9': $ctrl.highlighted,
                        'bCGFk': $ctrl.depth
                    }
                ]" ng-attr-is-pressed="{{$ctrl.pressed}}" title="49/1" is-best-selection="true" is-pressed="false">
                <!---->
                <!----><label ng-if="!$ctrl.isSp" class="Zs3u5 AUP11 Qe-26">50</label><!---->
                <!----><label ng-if="!$ctrl.isSp" class="He6+y Qe-26">R$132</label><!---->
            </button>
            </ours-price-button></td><!----><!----><!----><!----><!----><!----><!----><td class="bet-buttons lay-cell first-lay-cell" ng-repeat="lay in runner.toLay track by $index" ng-if="ctrl.vm.data.prefs.displayLayPrices &amp;&amp; runner.isActive &amp;&amp; (ctrl.vm.data.prefs.displayMarketDepth || $first)" ng-class="{   
                            'first-lay-cell': $first,
                            'suspended': ctrl.vm.data.market.isSuspended
                        }" bet-type="lay" bet-handicap="0" bet-selection-id="1222345"><ours-price-button type="lay" price="ctrl.vm.events.getBetPrice(lay.price)" size="ctrl.vm.events.getBetSize(lay.size, !$first)" depth="$index" pressed="$first &amp;&amp; runner.isLaySelected" highlightable="ctrl.vm.data.prefs.flashingUpdateButtonsEnabled" hover-text="ctrl.vm.events.getBetButtonFractionalOdd(lay)" disabled="ctrl.vm.data.market.isSuspended" on-click="ctrl.vm.events.addBet(ctrl.vm.data.betsConfiguration.types.lay, lay.price, runner)">
            <button class="_5iIjZ lay _4kgZU" ng-click="$ctrl.onClick()" ng-disabled="$ctrl.disabled" ng-attr-title="{{$ctrl.hoverText}}" ng-attr-is-best-selection="{{$ctrl.depth === 0}}" ng-attr-is-sp="{{$ctrl.isSp}}" ng-class="[
                    $ctrl.type,
                    {
                        'FfpPi': $ctrl.type === 'back',
                        '_4kgZU': $ctrl.type === 'lay',
                        'Sm8Nv': $ctrl.type === 'over',
                        'p0Mw+': $ctrl.type === 'under',
                        'SPkh1': $ctrl.pressed,
                        'd5UZ9': $ctrl.highlighted,
                        'bCGFk': $ctrl.depth
                    }
                ]" ng-attr-is-pressed="{{$ctrl.pressed}}" title="999/1" is-best-selection="true" is-pressed="false">
                <!---->
                <!----><label ng-if="!$ctrl.isSp" class="Zs3u5 AUP11 Qe-26">1000</label><!---->
                <!----><label ng-if="!$ctrl.isSp" class="He6+y Qe-26">R$68</label><!---->
            </button>
            </ours-price-button></td><!----><!----><!----><!----><!----><!----></tr><!----><!----><!----></tbody></table><!----></div></div></div></bf-marketview-runners-list><div class="suspended-overlay-container bf-col-1-1"><div class="suspended-overlay-wrapper"><span class="suspended-overlay"></span> <span class="suspended-label" translate="MARKETVIEW.STATUS.SUSPENDED">Suspenso</span></div></div></div><!----><!----><!----><a class="mini-mv-full-market-link mod-link" ng-transclude="" 
ng-if="miniMvCtrl.viewModel.market.eventTypeId" data-link-type="MARKET" data-event-type-id="1" data-market-id="1.216289833" ng-click="::miniMvCtrl.actions.onViewFullMarket()" href="football/market/1.216289833">Mostrar mercado completo<svg ng-attr-view_box="{{::viewBox}}" class="svg-icon-default arrow" data-icon="arrow-medium" 
data-style="arrow" viewBox="0 0 100 100"><path ng-attr-d="{{::getIconPath(icon)}}" d="M68.496,0.028L18.44,50.083l48.81,50.055l12.514-12.514L43.468,50.083l37.543-37.542 L68.496,0.028z"></path></svg></a><!---->
*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
<bf-marketview-header-wrapper market-id="miniMvCtrl.viewModel.marketId" market-name="miniMvCtrl.viewModel.market.name" event-type-id="miniMvCtrl.viewModel.market.eventTypeId" market-type="miniMvCtrl.viewModel.market.marketType" country-code="miniMvCtrl.viewModel.market.countryCode" is-closed="miniMvCtrl.viewModel.market.isClosed" inplay="miniMvCtrl.viewModel.market.inplay" in-play-enabled="miniMvCtrl.viewModel.market.inPlayEnabled" is-place-or-win="miniMvCtrl.viewModel.market.isPlaceOrWin" should-show-bsp="miniMvCtrl.viewModel.market.shouldShowBSP" is-ah="miniMvCtrl.viewModel.market.isAH" is-ah-double-line="miniMvCtrl.viewModel.market.isAHDoubleLine" is-over-asian-handicap-active-runners-limit="miniMvCtrl.viewModel.market.isOverAsianHandicapActiveRunnersLimit" theme="mini-marketview" gtm-module="miniMvCtrl.viewModel.gtmModule"><div class="marketview-header-wrapper-container bf-col-24-24"><div class="marketview-header-wrapper-bottom-container new-theme" ng-class="{      
            closed:
                ctrl.vm.data.market.isClosed,
            'has-favourites':
                ctrl.vm.data.hasFavourites,
            'new-theme': ctrl.vm.data.shouldUseNewTheme
         }"><!----><!----><marketview-header data="ctrl.vm.data"><div class="mv-header-container mini-marketview" ng-class="ctrl.data.marketHeaderTheme"><div class="mv-header-content"><div class="mv-header-main-section-wrapper"><!----><div class="market-name" ng-if="ctrl.data.marketHeaderTheme === 'mini-marketview' &amp;&amp; 
ctrl.data.marketNameSettings.visible"><span class="market-name-label" ng-bind="ctrl.data.marketNameSettings.label">Ambos os times marcam?</span></div><!----><div class="mv-header-main-section"><!----><div class="market-status mv-header-field market-inplay" ng-class="ctrl.data.marketStatus.class" ng-if="ctrl.data.marketStatus.visible"><span class="market-status-icon"></span> <!----></div><!----><!----><div class="cashout-availability mv-header-field" ng-if="ctrl.data.cashout.visible" ng-attr-title="{{::ctrl.data.cashout.tooltip}}" title="Cash out disponível neste mercado"><span class="cashout-icon"></span> <!----></div><!----><!----><span class="market-rules mv-header-field" ng-if="ctrl.data.marketRules.visible"><a class="market-rules-link" ng-click="ctrl.data.marketRules.onClick()"><span class="market-rules-icon"></span> <!----><span class="market-rules-label" ng-if="ctrl.data.marketRules.label" ng-bind="::ctrl.data.marketRules.label">Regras</span><!----></a></span><!----><!----><!----><!----><!----><!----></div></div><!----></div></div></marketview-header><div class="modal-dialog ng-hide" ng-show="show" show="ctrl.vm.data.contextualHelpPopup.show" width="300px"><div class="overlay" ng-click="hideDialog();"><div class="dialog-container"><div class="dialog" ng-style="dialogStyle" ng-click="$event.stopPropagation();" style="width: 300px;"><div class="dialog-header"><span class="dialog-title" ng-bind="modalDialogTitle"></span> <span class="close-dialog" ng-click="hideDialog()"></span></div><section class="dialog-content" ng-transclude=""><div class="sp-tooltip-text"><p ng-bind-template="Você pode optar por mostrar cotações ao Preço inicial Betfair (PIB). As apostas feitas com o preço inicial são liquidadas ao Preço inicial Betfair (PIB). Apostas ao Preço inicial Betfair (PIB) 
não podem ser canceladas quando feitas.">Você pode optar por mostrar cotações ao Preço inicial Betfair (PIB). As apostas feitas com o preço inicial são liquidadas ao Preço inicial Betfair (PIB). Apostas ao Preço inicial Betfair (PIB) não podem ser canceladas quando feitas.</p><p><a href="https://en-betfair.custhelp.com/app/answers/detail/a_id/421" ng-bind-template="Consulte a ajuda Preço inicial Betfair (PIB) para saber mais." target="_blank">Consulte a ajuda Preço inicial Betfair (PIB) 
para saber mais.</a></p></div></section></div></div></div></div></div><!----></div></bf-marketview-header-wrapper><!----><bf-cashout-wrapper market-id="miniMvCtrl.viewModel.marketId" event-type-id="miniMvCtrl.viewModel.market.eventTypeId" ga-module="miniMvCtrl.viewModel.gtmModule" bf-throttle="'cashout'"><!----></bf-cashout-wrapper><!-- end bfThrottle: 'cashout' --><!----><bf-runners-header ng-if="!miniMvCtrl.viewModel.isCollapsed" total-matched="miniMvCtrl.viewModel.market.totalMatched" is-closed="miniMvCtrl.viewModel.market.isClosed" back-label="A favor" lay-label="Contra"><table class="runners-header"><thead><tr class="rh-line" ng-class="{'without-lay': !rhCtrl.layLabel}"><th class="rh-runner-name-header"><!----><span class="rh-matched-amount-label" ng-if="rhCtrl.vm.data.marketMatched.visible" ng-bind-template="Correspondido: BRL 23,774">Correspondido: BRL 23,774</span><!----> <!----> <!----></th><!----><!----><!----><th ng-if="rhCtrl.backLabel" ng-class="{'is-small': !rhCtrl.displayMarketDepth}" class="rh-label-all is-small"><span class="rh-label-back" ng-bind-template="A favor">A favor</span></th><!----><!----><!----><!----><th ng-if="rhCtrl.layLabel" ng-class="{'is-small': !rhCtrl.displayMarketDepth}" class="rh-label-all is-small"><span class="rh-label-lay" ng-bind-template="Contra">Contra</span></th><!----><!----></tr></thead></table></bf-runners-header><!----><!----><div ng-if="!miniMvCtrl.viewModel.isCollapsed" class="mini-mv-runners-list-wrapper" suspended-overlay="miniMvCtrl.viewModel.market.isSuspended"><bf-marketview-runners-list is-bsp-reconciled="miniMvCtrl.viewModel.market.bspReconciled" country-code="miniMvCtrl.viewModel.market.countryCode" event-type-id="miniMvCtrl.viewModel.market.eventTypeId" has-pnl-inline="miniMvCtrl.viewModel.market.hasPnlInline" market-id="miniMvCtrl.viewModel.marketId" is-ah-double-line="miniMvCtrl.viewModel.market.isAHDoubleLine" is-closed="miniMvCtrl.viewModel.market.isClosed" is-hr="miniMvCtrl.viewModel.market.isHR" is-gh="miniMvCtrl.viewModel.market.isGH" is-place-or-win="miniMvCtrl.viewModel.market.isPlaceOrWin" is-saddlecloth-racing="miniMvCtrl.viewModel.market.isSaddleclothRacing" is-suspended="miniMvCtrl.viewModel.market.isSuspended" inplay="miniMvCtrl.viewModel.market.inplay" market-type="miniMvCtrl.viewModel.market.marketType" display-lay-prices="miniMvCtrl.viewModel.preferences.displayLayPrices" display-profit-and-loss="miniMvCtrl.viewModel.preferences.displayProfitAndLoss" display-future-profit-and-loss="miniMvCtrl.viewModel.preferences.displayFutureProfitAndLoss" enable-flashing-update-buttons="miniMvCtrl.viewModel.preferences.flashingUpdateButtonsEnabled" show-fractional-odds="miniMvCtrl.viewModel.preferences.showFractionalOdds" display-market-depth="::miniMvCtrl.viewModel.preferences.displayMarketDepth" display-race-card-info="::miniMvCtrl.viewModel.preferences.displayRaceCardInfo" display-sp-bets="::miniMvCtrl.viewModel.preferences.displaySPBets" display-sp-bets-near-far="::miniMvCtrl.viewModel.preferences.displaySPBetsNearFar" display-sp-bets-none="::miniMvCtrl.viewModel.preferences.displaySPBetsNone" 
display-sp-bets-projected-odds="::miniMvCtrl.viewModel.preferences.displaySPBetsProjectedOdds" display-timeform123="false" runners="miniMvCtrl.viewModel.runners" pnl="miniMvCtrl.viewModel.pnl" on-add-bet="miniMvCtrl.actions.addBet(betType, price, runner)" inline-betting-state="miniMvCtrl.viewModel.inlineBettingState"><div class="marketview-list-runners-component bf-row"><div class="runners-container bf-col-24-24"><div class="mv-runner-list-container overlayPosition"><bf-overlay ng-show="ctrl.vm.data.settings.overlayCashOutMessage" elem="'.mv-runner-list-container'" class="bf-overlay runner-list-overlay ng-hide"></bf-overlay><table class="mv-runner-list fixed-size" ng-class="{
                       'aus-greyhounds': ctrl.vm.data.isAusGreyhounds,
                       'fixed-size': !ctrl.vm.data.prefs.displayMarketDepth,
                       'market-closed': ctrl.vm.data.market.isClosed,
                       'small': ctrl.vm.data.isSmallTable,
                       'large': ctrl.vm.data.isLargeTable
                   }"><tbody><!----><tr class="runner-line" ng-repeat-start="runner in ctrl.vm.data.runners | filter:{isVisibleOnMarket:true} track by runner.key" ng-class="{
                        'loser-runner': runner.isLoser,
                        'removed-runner': runner.isRemoved || runner.isRemovedVacant,
                        'winner-runner': runner.isWinner || runner.isPlaced
                    }"><!----><td class="new-runner-info" ng-class="{
                            'with-pin-runners': ctrl.pinRunnersEditMode,
                            'without-lay': !ctrl.vm.data.prefs.displayLayPrices,
                            'with-runner-timeform-info': ctrl.vm.data.prefs.displayTimeform123 &amp;&amp; runner.isActive &amp;&amp; ctrl.vm.data.timeformRunners[runner.selectionId]
                        }" colspan="" ng-click="::ctrl.vm.events.runnerInfoDropdownClick(runner.selectionId, runner.isActive)"><!----><!----><div class="runner-info-container"><div class="market-graph-container"><!----><bf-market-graph market-id="::ctrl.vm.data.market.id" selection-id="::runner.selectionId" handicap="::runner.handicap" ng-click="ctrl.vm.events.handleOpenedGraphGTM($event);" ng-if="runner.isActive &amp;&amp; ctrl.vm.data.market.eventTypeId" on-graph-window-closed="ctrl.vm.events.handleGraphWindowClosed();"><button class="market-graph" ng-click="ctrl.vm.events.openMarketGraph()"></button></bf-market-graph><!----></div><div class="runner-data-container without-race-card-info" ng-class="{
                                    'with-pnl': ctrl.vm.events.shouldShowPnl(runner),
                                    'without-race-card-info': !ctrl.vm.data.displayRaceCardInfo
                                 }"><bf-runner-info ng-class="ctrl.vm.data.market.isSaddleclothRacing ? 'name-saddlecloth' : 'name-silk'" type="default" runner="::runner" metadata="ctrl.vm.data.runnerMetadataMap[runner.selectionId]" show-race-card="ctrl.vm.data.displayRaceCardInfo" is-saddle-cloth-racing="ctrl.vm.data.market.isSaddleclothRacing" class="name-silk"><div ng-switch="::$ctrl.type" class="runner-info"><!----><!----><!----><div ng-switch-default="" class="default name"><h3 class="runner-name" ng-bind="$ctrl.runnerName">Sim</h3></div><!----></div></bf-runner-info></div><!----></div></td><!----><!----><!----><!----><!----><!----><td class="bet-buttons back-cell last-back-cell" ng-repeat="back in runner.toBack track by $index" ng-if="runner.isActive &amp;&amp; (ctrl.vm.data.prefs.displayMarketDepth || 
$last)" ng-class="{
                            'last-back-cell': $last,
                            'suspended': ctrl.vm.data.market.isSuspended,
                            'without-lay': !ctrl.vm.data.prefs.displayLayPrices
                        }" bet-type="back" bet-is-sp="false" bet-handicap="0" bet-selection-id="30246"><ours-price-button type="back" price="ctrl.vm.events.getBetPrice(back.price)" size="ctrl.vm.events.getBetSize(back.size, !$last)" depth="runner.toBack.length - $index - 1" pressed="$last &amp;&amp; runner.isBackSelected" highlightable="ctrl.vm.data.prefs.flashingUpdateButtonsEnabled" hover-text="ctrl.vm.events.getBetButtonFractionalOdd(back)" disabled="ctrl.vm.data.market.isSuspended" on-click="ctrl.vm.events.addBet(ctrl.vm.data.betsConfiguration.types.back, back.price, runner)">
            <button class="_5iIjZ back FfpPi" ng-click="$ctrl.onClick()" ng-disabled="$ctrl.disabled" ng-attr-title="{{$ctrl.hoverText}}" ng-attr-is-best-selection="{{$ctrl.depth === 0}}" ng-attr-is-sp="{{$ctrl.isSp}}" ng-class="[
                    $ctrl.type,
                    {
                        'FfpPi': $ctrl.type === 'back',
                        '_4kgZU': $ctrl.type === 'lay',
                        'Sm8Nv': $ctrl.type === 'over',
                        'p0Mw+': $ctrl.type === 'under',
                        'SPkh1': $ctrl.pressed,
                        'd5UZ9': $ctrl.highlighted,
                        'bCGFk': $ctrl.depth
                    }
                ]" ng-attr-is-pressed="{{$ctrl.pressed}}" title="4/1" is-best-selection="true" is-pressed="false">
                <!---->
                <!----><label ng-if="!$ctrl.isSp" class="Zs3u5 AUP11 Qe-26">5</label><!---->
                <!----><label ng-if="!$ctrl.isSp" class="He6+y Qe-26">R$285</label><!---->
            </button>
            </ours-price-button></td><!----><!----><!----><!----><!----><!----><!----><td class="bet-buttons lay-cell first-lay-cell" ng-repeat="lay in runner.toLay track by $index" ng-if="ctrl.vm.data.prefs.displayLayPrices &amp;&amp; runner.isActive &amp;&amp; (ctrl.vm.data.prefs.displayMarketDepth || $first)" ng-class="{   
                            'first-lay-cell': $first,
                            'suspended': ctrl.vm.data.market.isSuspended
                        }" bet-type="lay" bet-handicap="0" bet-selection-id="30246"><ours-price-button type="lay" price="ctrl.vm.events.getBetPrice(lay.price)" size="ctrl.vm.events.getBetSize(lay.size, !$first)" depth="$index" pressed="$first &amp;&amp; runner.isLaySelected" highlightable="ctrl.vm.data.prefs.flashingUpdateButtonsEnabled" hover-text="ctrl.vm.events.getBetButtonFractionalOdd(lay)" disabled="ctrl.vm.data.market.isSuspended" on-click="ctrl.vm.events.addBet(ctrl.vm.data.betsConfiguration.types.lay, lay.price, runner)">
            <button class="_5iIjZ lay _4kgZU" ng-click="$ctrl.onClick()" ng-disabled="$ctrl.disabled" ng-attr-title="{{$ctrl.hoverText}}" ng-attr-is-best-selection="{{$ctrl.depth === 0}}" ng-attr-is-sp="{{$ctrl.isSp}}" ng-class="[
                    $ctrl.type,
                    {
                        'FfpPi': $ctrl.type === 'back',
                        '_4kgZU': $ctrl.type === 'lay',
                        'Sm8Nv': $ctrl.type === 'over',
                        'p0Mw+': $ctrl.type === 'under',
                        'SPkh1': $ctrl.pressed,
                        'd5UZ9': $ctrl.highlighted,
                        'bCGFk': $ctrl.depth
                    }
                ]" ng-attr-is-pressed="{{$ctrl.pressed}}" title="" is-best-selection="true" is-pressed="false">
                <!---->
                <!----><label ng-if="!$ctrl.isSp" class="Zs3u5 AUP11 Qe-26"></label><!---->
                <!----><label ng-if="!$ctrl.isSp" class="He6+y Qe-26"></label><!---->
            </button>
            </ours-price-button></td><!----><!----><!----><!----><!----><!----></tr><!----><!----><!----><tr class="runner-line" ng-repeat-start="runner in ctrl.vm.data.runners | filter:{isVisibleOnMarket:true} track by runner.key" ng-class="{
                        'loser-runner': runner.isLoser,
                        'removed-runner': runner.isRemoved || runner.isRemovedVacant,
                        'winner-runner': runner.isWinner || runner.isPlaced
                    }"><!----><td class="new-runner-info" ng-class="{
                            'with-pin-runners': ctrl.pinRunnersEditMode,
                            'without-lay': !ctrl.vm.data.prefs.displayLayPrices,
                            'with-runner-timeform-info': ctrl.vm.data.prefs.displayTimeform123 &amp;&amp; runner.isActive &amp;&amp; ctrl.vm.data.timeformRunners[runner.selectionId]
                        }" colspan="" ng-click="::ctrl.vm.events.runnerInfoDropdownClick(runner.selectionId, runner.isActive)"><!----><!----><div class="runner-info-container"><div class="market-graph-container"><!----><bf-market-graph market-id="::ctrl.vm.data.market.id" selection-id="::runner.selectionId" handicap="::runner.handicap" ng-click="ctrl.vm.events.handleOpenedGraphGTM($event);" ng-if="runner.isActive &amp;&amp; ctrl.vm.data.market.eventTypeId" on-graph-window-closed="ctrl.vm.events.handleGraphWindowClosed();"><button class="market-graph" ng-click="ctrl.vm.events.openMarketGraph()"></button></bf-market-graph><!----></div><div class="runner-data-container without-race-card-info" ng-class="{
                                    'with-pnl': ctrl.vm.events.shouldShowPnl(runner),
                                    'without-race-card-info': !ctrl.vm.data.displayRaceCardInfo
                                 }"><bf-runner-info ng-class="ctrl.vm.data.market.isSaddleclothRacing ? 'name-saddlecloth' : 'name-silk'" type="default" runner="::runner" metadata="ctrl.vm.data.runnerMetadataMap[runner.selectionId]" show-race-card="ctrl.vm.data.displayRaceCardInfo" is-saddle-cloth-racing="ctrl.vm.data.market.isSaddleclothRacing" class="name-silk"><div ng-switch="::$ctrl.type" class="runner-info"><!----><!----><!----><div ng-switch-default="" class="default name"><h3 class="runner-name" ng-bind="$ctrl.runnerName">Não</h3></div><!----></div></bf-runner-info></div><!----></div></td><!----><!----><!----><!----><!----><!----><td class="bet-buttons back-cell last-back-cell" ng-repeat="back in runner.toBack track by $index" ng-if="runner.isActive &amp;&amp; (ctrl.vm.data.prefs.displayMarketDepth || 
$last)" ng-class="{
                            'last-back-cell': $last,
                            'suspended': ctrl.vm.data.market.isSuspended,
                            'without-lay': !ctrl.vm.data.prefs.displayLayPrices
                        }" bet-type="back" bet-is-sp="false" bet-handicap="0" bet-selection-id="110503"><ours-price-button type="back" price="ctrl.vm.events.getBetPrice(back.price)" size="ctrl.vm.events.getBetSize(back.size, !$last)" depth="runner.toBack.length - $index - 1" pressed="$last &amp;&amp; runner.isBackSelected" highlightable="ctrl.vm.data.prefs.flashingUpdateButtonsEnabled" hover-text="ctrl.vm.events.getBetButtonFractionalOdd(back)" disabled="ctrl.vm.data.market.isSuspended" 
on-click="ctrl.vm.events.addBet(ctrl.vm.data.betsConfiguration.types.back, back.price, runner)">
            <button class="_5iIjZ back FfpPi" ng-click="$ctrl.onClick()" ng-disabled="$ctrl.disabled" ng-attr-title="{{$ctrl.hoverText}}" ng-attr-is-best-selection="{{$ctrl.depth === 0}}" ng-attr-is-sp="{{$ctrl.isSp}}" ng-class="[
                    $ctrl.type,
                    {
                        'FfpPi': $ctrl.type === 'back',
                        '_4kgZU': $ctrl.type === 'lay',
                        'Sm8Nv': $ctrl.type === 'over',
                        'p0Mw+': $ctrl.type === 'under',
                        'SPkh1': $ctrl.pressed,
                        'd5UZ9': $ctrl.highlighted,
                        'bCGFk': $ctrl.depth
                    }
                ]" ng-attr-is-pressed="{{$ctrl.pressed}}" title="1/100" is-best-selection="true" is-pressed="false">
                <!---->
                <!----><label ng-if="!$ctrl.isSp" class="Zs3u5 AUP11 Qe-26">1.01</label><!---->
                <!----><label ng-if="!$ctrl.isSp" class="He6+y Qe-26">R$89</label><!---->
            </button>
            </ours-price-button></td><!----><!----><!----><!----><!----><!----><!----><td class="bet-buttons lay-cell first-lay-cell" ng-repeat="lay in runner.toLay track by $index" ng-if="ctrl.vm.data.prefs.displayLayPrices &amp;&amp; runner.isActive &amp;&amp; (ctrl.vm.data.prefs.displayMarketDepth || $first)" ng-class="{   
                            'first-lay-cell': $first,
                            'suspended': ctrl.vm.data.market.isSuspended
                        }" bet-type="lay" bet-handicap="0" bet-selection-id="110503"><ours-price-button type="lay" price="ctrl.vm.events.getBetPrice(lay.price)" size="ctrl.vm.events.getBetSize(lay.size, !$first)" depth="$index" pressed="$first &amp;&amp; runner.isLaySelected" highlightable="ctrl.vm.data.prefs.flashingUpdateButtonsEnabled" hover-text="ctrl.vm.events.getBetButtonFractionalOdd(lay)" disabled="ctrl.vm.data.market.isSuspended" on-click="ctrl.vm.events.addBet(ctrl.vm.data.betsConfiguration.types.lay, lay.price, runner)">
            <button class="_5iIjZ lay _4kgZU" ng-click="$ctrl.onClick()" ng-disabled="$ctrl.disabled" ng-attr-title="{{$ctrl.hoverText}}" ng-attr-is-best-selection="{{$ctrl.depth === 0}}" ng-attr-is-sp="{{$ctrl.isSp}}" ng-class="[
                    $ctrl.type,
                    {
                        'FfpPi': $ctrl.type === 'back',
                        '_4kgZU': $ctrl.type === 'lay',
                        'Sm8Nv': $ctrl.type === 'over',
                        'p0Mw+': $ctrl.type === 'under',
                        'SPkh1': $ctrl.pressed,
                        'd5UZ9': $ctrl.highlighted,
                        'bCGFk': $ctrl.depth
                    }
                ]" ng-attr-is-pressed="{{$ctrl.pressed}}" title="1/12" is-best-selection="true" is-pressed="false">
                <!---->
                <!----><label ng-if="!$ctrl.isSp" class="Zs3u5 AUP11 Qe-26">1.08</label><!---->
                <!----><label ng-if="!$ctrl.isSp" class="He6+y Qe-26">R$613</label><!---->
            </button>
            </ours-price-button></td><!----><!----><!----><!----><!----><!----></tr><!----><!----><!----></tbody></table><!----></div></div></div></bf-marketview-runners-list><div class="suspended-overlay-container bf-col-1-1"><div class="suspended-overlay-wrapper"><span class="suspended-overlay"></span> <span class="suspended-label" translate="MARKETVIEW.STATUS.SUSPENDED">Suspenso</span></div></div></div><!----><!----><!----><a class="mini-mv-full-market-link mod-link" ng-transclude="" 
ng-if="miniMvCtrl.viewModel.market.eventTypeId" data-link-type="MARKET" data-event-type-id="1" data-market-id="1.216289868" ng-click="::miniMvCtrl.actions.onViewFullMarket()" href="football/market/1.216289868">Mostrar mercado completo<svg ng-attr-view_box="{{::viewBox}}" class="svg-icon-default arrow" data-icon="arrow-medium" 
data-style="arrow" viewBox="0 0 100 100"><path ng-attr-d="{{::getIconPath(icon)}}" d="M68.496,0.028L18.44,50.083l48.81,50.055l12.514-12.514L43.468,50.083l37.543-37.542 L68.496,0.028z"></path></svg></a><!---->"""


def extract_ng_bind_value_from_html(html, expression):
    # Analisa o HTML usando BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Encontra o elemento que contém a expressão ng-bind especificada
    element = soup.find(attrs={"ng-bind": expression})

    if element:
        # Obtém o valor do atributo ng-bind
        ng_bind_value = element.get("ng-bind")
        return ng_bind_value

    return None

def extract_ng_bind_value(html):
    # Analisa o HTML usando BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Encontra o elemento que contém o atributo "ng-bind" com o valor desejado
    element = soup.find_all(attrs={"ng-bind": "ctrl.data.marketNameSettings.label"})

    # if element:
    #     return element.get_text().strip()
    # else:
    #     return None
    for li in element:
        print(li.text)

def extract_table_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    table_data = []

    # Encontra todas as linhas da tabela (tr)
    rows = soup.find_all('tr')

    for row in rows:
        row_data = []
        # Encontra todas as colunas da linha (td)
        cols = row.find_all(['th', 'td'])
        for col in cols:
            # Adiciona o texto de cada coluna à lista de dados da linha
            row_data.append(col.get_text(strip=True))
        table_data.append(row_data)

    return table_data

# Obtém os dados da tabela
table_data = extract_table_data(tabela)

# Cria um DataFrame a partir dos dados da tabela
df = pd.DataFrame(table_data)

# Imprime o DataFrame
print(df)
# expression = "ctrl.data.marketNameSettings.label"
value = extract_ng_bind_value(tabela)
# print(value)
mercado  = [value]
df['mercado'] = mercado
print(df)