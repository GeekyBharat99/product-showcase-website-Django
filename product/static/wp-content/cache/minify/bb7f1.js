(function(){var a=function(){var a,b;return b=document.createElement("script"),b.src=_zxcvbnSettings.src,b.type="text/javascript",b.async=!0,a=document.getElementsByTagName("script")[0],a.parentNode.insertBefore(b,a)};null!=window.attachEvent?window.attachEvent("onload",a):window.addEventListener("load",a,!1)}).call(this);
;jQuery(function(){jQuery(":input").on("focus",function(){var input=jQuery(this);var inputID=input.attr("id")||"(no input ID)";var inputName=input.attr("name")||"(no input name)";var inputClass=input.attr("class")||"(no input class)";var form=jQuery(this.form);var formID=form.attr("id")||"(no form ID)";var formName=form.attr("name")||"(no form name)";var formClass=form.attr("class")||"(no form class)";window[gtm4wp_datalayer_name].push({'event':'gtm4wp.formElementEnter','inputID':inputID,'inputName':inputName,'inputClass':inputClass,'formID':formID,'formName':formName,'formClass':formClass});}).on("blur",function(){var input=jQuery(this);var inputID=input.attr("id")||"(no input ID)";var inputName=input.attr("name")||"(no input name)";var inputClass=input.attr("class")||"(no input class)";var form=jQuery(this.form);var formID=form.attr("id")||"(no form ID)";var formName=form.attr("name")||"(no form name)";var formClass=form.attr("class")||"(no form class)";window[gtm4wp_datalayer_name].push({'event':'gtm4wp.formElementLeave','inputID':inputID,'inputName':inputName,'inputClass':inputClass,'formID':formID,'formName':formName,'formClass':formClass});});});;(function($){'use strict';$(document).ready(function(){$('body').on('adding_to_cart',function(event,$button,data){if($button&&$button.hasClass('vc_gitem-link')){$button.addClass('vc-gitem-add-to-cart-loading-btn').parents('.vc_grid-item-mini').addClass('vc-woocommerce-add-to-cart-loading').append($('<div class="vc_wc-load-add-to-loader-wrapper"><div class="vc_wc-load-add-to-loader"></div></div>'));}}).on('added_to_cart',function(event,fragments,cart_hash,$button){if('undefined'===typeof($button)){$button=$('.vc-gitem-add-to-cart-loading-btn');}
if($button&&$button.hasClass('vc_gitem-link')){$button.removeClass('vc-gitem-add-to-cart-loading-btn').parents('.vc_grid-item-mini').removeClass('vc-woocommerce-add-to-cart-loading').find('.vc_wc-load-add-to-loader-wrapper').remove();}});});})(window.jQuery);