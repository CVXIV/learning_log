(function($){
    $.fn.validationEngineLanguage = function(){
    };
    $.validationEngineLanguage = {
        newLang: function(){
            $.validationEngineLanguage.allRules = {
                "required": { // Add your regex rules here, you can take telephone as an example
                    "regex": "none",
                    "alertText": "* 此处不可空白",
                    "alertTextSelect": "* 请选择",
                    "alertTextCheckboxMultiple": "* 请选择一个项目",
                    "alertTextCheckboxe": "* 您必须钩选此栏",
                    "alertTextDateRange": "* 日期范围不可空白"
                },
				"checkpass": {//密码强度校验
                    "regex":/(?=(?:.*?[a-zA-Z]){1})(?=(?:.*?\d){1})/,//不强制含特殊字符(?=(?:.*?[!@#$%*()_+^&}{:;?.]){1})
                    "alertText": "* 必须包含数字与字母"
                },
                "pwdedit":{
                	"regex":/^(?![^a-zA-Z]+$)(?!\D+$).{8,}$/,
                	"alertText": "* 必须为8位或8位以上数字和字母的组合"
                },
                "dateRange": {
                    "regex": "none",
                    "alertText": "* 无效的 ",
                    "alertText2": " 日期范围"
                },
                "dateTimeRange": {
                    "regex": "none",
                    "alertText": "* 无效的 ",
                    "alertText2": " 时间范围"
                },
                "minSize": {
                    "regex": "none",
                    "alertText": "* 最少 ",
                    "alertText2": " 个字符"
                },
                "maxSize": {
                    "regex": "none",
                    "alertText": "* 最多 ",
                    "alertText2": " 个字符"
                },
                "maxUtf8Size": {
                    "regex": "none",
                    "alertText": "* 最多 ",
                    "alertText2": " 个字符或",
                    "alertText3": " 个汉字"
                },
				"groupRequired": {
                    "regex": "none",
                    "alertText": "* 你必须选填其中一个栏位"
                },
                "min": {
                    "regex": "none",
                    "alertText": "* 最小值为 "
                },
                "max": {
                    "regex": "none",
                    "alertText": "* 最大值为 "
                },
                "past": {
                    "regex": "none",
                    "alertText": "* 日期必须早于 "
                },
                "future": {
                    "regex": "none",
                    "alertText": "* 日期必须晚于 "
                },	
                "maxCheckbox": {
                    "regex": "none",
                    "alertText": "* 最多选取 ",
                    "alertText2": " 个项目"
                },
                "minCheckbox": {
                    "regex": "none",
                    "alertText": "* 至少 ",
                    "alertText2": " 个项目"
                },
                "equals": {
                    "regex": "none",
                    "alertText": "* 请输入与上面相同的密码"
                },
                "noEquals": {
                    "regex": "none",
                    "alertText": "* 请输入与其他门禁不同的名称"
                },
                "creditCard": {
                    "regex": "none",
                    "alertText": "* 无效的信用卡号码"
                },
                "bankCard": {
                    "regex": /^[0-9]{19}$/,
                    "alertText": "* 无效的银行卡号码"
                },
				//added by zhoujunyang start
				"postCode": {
                    "regex": /^[0-9]{6}$/,
                    "alertText": "* 邮编格式不正确"
                },
				"fax": {//验证座机电话和传真 
                    "regex": /^(([0\+]\d{2,3}-)?(0\d{2,3})-)(\d{7,8})(-(\d{1,6}))?$/,
                    "alertText": "* 格式不正确,正确格式:区号-电话号码-分机"
                },
				//added by zhoujunyang end
                "phone": {
                    // credit: jquery.h5validate.js / orefalo
                   // "regex": /^([\+][0-9]{1,3}[ \.\-])?([\(]{1}[0-9]{2,6}[\)])?([0-9 \.\-\/]{3,20})((x|ext|extension)[ ]?[0-9]{1,4})?$/,
				   //"regex": /^(1[3458][0-9]{8})|(0[0-9]{}-?)$/,
                	"regex": /^((1[34578][0-9]{9})|(((0[12][0-9]-[1-9][0-9]{7})|(0[3-9][0-9]{2}-[1-9][0-9]{6,7}))(-[0-9]{3,5})?))$/,
                    "alertText": "* 请输入有效的电话号码"
                },
                "simplePhone": {
                    // credit: jquery.h5validate.js / orefalo
                   // "regex": /^([\+][0-9]{1,3}[ \.\-])?([\(]{1}[0-9]{2,6}[\)])?([0-9 \.\-\/]{3,20})((x|ext|extension)[ ]?[0-9]{1,4})?$/,
				   //"regex": /^(0|86|17951)?(13[0-9]|15[012356789]|18[0236789]|14[57])[0-9]{8}$/,
				   "regex": /^([-0123456789]){5,30}$/,
                    "alertText": "* 请输入有效的电话号码"
                },
                "email": {
                    // Shamelessly lifted from Scott Gonzalez via the Bassistance Validation plugin http://projects.scottsplayground.com/email_address_validation/
                    "regex": /^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i,
                    "alertText": "* 邮件地址无效"
                },
                "integer": {
                    "regex": /^[\-\+]?\d+$/,
                    "alertText": "* 不是有效的整数"
                },
				"bill_rate": {
                    "regex": /^\d+(\.\d+)?$/,
                    "alertText": "* 请输入正确格式的利率"
                },
				"decimal": {
                    "regex": /^\d+(\.\d+)?$/,
                    "alertText": "* 请输入正确格式的数字"
                },
				"bill_amnt": {
                    "regex": /^[\-\+]?\d+(\.\d{1,2})?$/,
                    "alertText": "* 最多支持2位小数"
                },
                "a_decimal": {
                	"regex": /^\d+(\.\d{1})?$/,
                	"alertText": "* 最多支持1位小数"
                },
                "bill_price": {
                    "regex": /^\d+(\.\d{1,2})?$/,
                    "alertText": "* 请输入正确格式的金额"
                },
                "b_decimal": {
                    "regex": /^\d+(\.\d{1,2})?$/,
                    "alertText": "* 最多支持2位小数的正数"
                },
                "number": {
                    // Number, including positive, negative, and floating decimal. credit: orefalo
                    "regex": /^[\-\+]?(([0-9]+)([\.,]([0-9]+))?|([\.,]([0-9]+))?)$/,
                    "alertText": "* 无效的数字"
                },
                "date": {
                    "regex": /^\d{4}[\/\-](0?[1-9]|1[012])[\/\-](0?[1-9]|[12][0-9]|3[01])$/,
                    "alertText": "* 无效的日期，格式必须为 YYYY-MM-DD"
                },
				//added by zhoujunyang start
				"date2": {
                    "regex": /^\d{4}(0?[1-9]|1[012])(0?[1-9]|[12][0-9]|3[01])$/,
                    "alertText": "* 无效的日期，格式必须为YYYYMMDD "
                },
				//added by zhoujunyang end
                "ipv4": {
                    "regex": /^((([01]?[0-9]{1,2})|(2[0-4][0-9])|(25[0-5]))[.]){3}(([0-1]?[0-9]{1,2})|(2[0-4][0-9])|(25[0-5]))$/,
                    "alertText": "* 无效的 IP 地址"
                },
                "url": {
                    "regex": /^(https?|ftp):\/\/(((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:)*@)?(((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]))|((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?)(:\d*)?)(\/((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)+(\/(([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)*)*)?)?(\?((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|[\uE000-\uF8FF]|\/|\?)*)?(\#((([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|\/|\?)*)?$/i,
                    "alertText": "* 无效的 URL"
                },
                "onlyNumberSp": {
                    "regex": /^[1-9][0-9]*$/,
                    "alertText": "* 只能填正整数"
                },
                "onlyNumber": {   
                	"regex": /^[0-9]+$/,   
                	"alertText": "* 只能填正整数"
                }, 
                "onlyLetterSp": {
                    "regex": /^[a-zA-Z\ \']+$/,
                    "alertText": "* 只接受英文字母大小写"
                },
                "onlyLetterNumber": {
                    "regex": /^[0-9a-zA-Z]+$/,
                    "alertText": "* 不接受特殊字符"
                },
				"onlyChinese": {
                    "regex": /^[\u4E00-\u9FA5]/g,
                    "alertText": "* 只能输入中文"
                },
                // --- CUSTOM RULES -- Those are specific to the demos, they can be removed or changed to your likings
                "ajaxUserCall": {
                    "url": "ajaxValidateFieldUser",
                    // you may want to pass extra data on the ajax call
                    "extraData": "name=eric",
                    "alertText": "* 此名称已被其他人使用",
                    "alertTextLoad": "* 正在确认名称是否有其他人使用，请稍等。"
                },
				"ajaxUserCallPhp": {
                    "url": "phpajax/ajaxValidateFieldUser.php",
                    // you may want to pass extra data on the ajax call
                    "extraData": "name=eric",
                    // if you provide an "alertTextOk", it will show as a green prompt when the field validates
                    "alertTextOk": "* 此帐号名称可以使用",
                    "alertText": "* 此名称已被其他人使用",
                    "alertTextLoad": "* 正在确认帐号名称是否有其他人使用，请稍等。"
                },
                "ajaxNameCall": {
                    // remote json service location
                    "url": "idCheck",
                    // error
                    "alertText": "* 已存在相同的设备ID!",
                    // if you provide an "alertTextOk", it will show as a green prompt when the field validates
                    "alertTextOk": "* 此设备ID可以使用!"
                },
				 "ajaxNameCallPhp": {
	                    // remote json service location
	                    "url": "/NewChinaCp/user/validateAcntNo.action",
	                    // error
	                    "alertText": "* 此名称已被其他人使用",
	                    // speaks by itself
	                    "alertTextLoad": "* 正在确认名称是否有其他人使用，请稍等。"
	                },
                "ajaxSourceNo": {
                    // remote json service location
                    "url": "testSourceTypeAction.action",
                    // error
                    "alertText": "* 来源单号不存在！",
                    "alertText2": "* 来源单号已经存在！",
                    "alertTextOk": "* 验证通过！",
                    // speaks by itself
                    "alertTextLoad": "* 正在确认来源单号是否存在，请稍等。"
                },
                "CN": {
                    "regex":/^.{0,}[\u4E00-\u9FA5]{1,}.{0,}$/,
                    "alertText":"* 必须包含中文！"
                },
                "noCN": {
                    "regex":/^[^\u4E00-\u9FA5]{0,}$/,
                    "alertText":"* 不能包含中文！"
                },
                "validate2fields": {
                    "alertText": "* 请输入 HELLO"
                },
	            //tls warning:homegrown not fielded 
                "dateFormat":{
                    "regex": /^\d{4}[\/\-](0?[1-9]|1[012])[\/\-](0?[1-9]|[12][0-9]|3[01])$|^(?:(?:(?:0?[13578]|1[02])(\/|-)31)|(?:(?:0?[1,3-9]|1[0-2])(\/|-)(?:29|30)))(\/|-)(?:[1-9]\d\d\d|\d[1-9]\d\d|\d\d[1-9]\d|\d\d\d[1-9])$|^(?:(?:0?[1-9]|1[0-2])(\/|-)(?:0?[1-9]|1\d|2[0-8]))(\/|-)(?:[1-9]\d\d\d|\d[1-9]\d\d|\d\d[1-9]\d|\d\d\d[1-9])$|^(0?2(\/|-)29)(\/|-)(?:(?:0[48]00|[13579][26]00|[2468][048]00)|(?:\d\d)?(?:0[48]|[2468][048]|[13579][26]))$/,
                    "alertText": "* 无效的日期格式"
                },
                //tls warning:homegrown not fielded 
				"dateTimeFormat": {
	                "regex": /^\d{4}[\/\-](0?[1-9]|1[012])[\/\-](0?[1-9]|[12][0-9]|3[01])\s+(1[012]|0?[1-9]){1}:(0?[1-5]|[0-6][0-9]){1}:(0?[0-6]|[0-6][0-9]){1}\s+(am|pm|AM|PM){1}$|^(?:(?:(?:0?[13578]|1[02])(\/|-)31)|(?:(?:0?[1,3-9]|1[0-2])(\/|-)(?:29|30)))(\/|-)(?:[1-9]\d\d\d|\d[1-9]\d\d|\d\d[1-9]\d|\d\d\d[1-9])$|^((1[012]|0?[1-9]){1}\/(0?[1-9]|[12][0-9]|3[01]){1}\/\d{2,4}\s+(1[012]|0?[1-9]){1}:(0?[1-5]|[0-6][0-9]){1}:(0?[0-6]|[0-6][0-9]){1}\s+(am|pm|AM|PM){1})$/,
                    "alertText": "* 无效的日期或时间格式",
                    "alertText2": "可接受的格式： ",
                    "alertText3": "mm/dd/yyyy hh:mm:ss AM|PM 或 ", 
                    "alertText4": "yyyy-mm-dd hh:mm:ss AM|PM"
	            },
	            //check number combine letter
	            "checkNumberAndLetter" : {
	            	"regex": /^[A-Za-z].*[0-9]|[0-9].*[A-Za-z]$/,
                    "alertText": "* 请输入字母和数字的组合"
	            },
	            "checkCnAndEnAndNum": {
	            	"regex": /^[0-9a-zA-Z \u4E00-\u9FA5]+$/, /* 正则表达式，如果正则能匹配内容表示通过 */
	            	"alertText": "* 请输入中文、英文、数字的组合"
	            },
	            //added by huangyifan start
	            "checkBlank" : {
	            	"regex": /^[^ ]+$/,
	            	"alertText":"* 不能输入空格！"
	            },
	            //added by huangyifan end
	            
	            "checkSpecialCharacter":{
	            	"regex": /^[^\/\\\[\]%_\^]+$/,
	            	"alertText":"不能输入特殊字符，如：\\、/、[、]、%、_、^"
	            }
            };
            
        }
    };
    $.validationEngineLanguage.newLang();
})(jQuery);
