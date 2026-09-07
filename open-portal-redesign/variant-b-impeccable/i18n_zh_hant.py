# -*- coding: utf-8 -*-
"""
Traditional Chinese copy for the Direction B portal pages.

Written for Taiwan/Hong Kong readers, not converted glyph-for-glyph from the
Simplified text. The regional IT and travel vocabulary differs, and a converter
would have produced mainland phrasing in Traditional characters:

  介面 not 接口     資料 not 數據     伺服器 not 服務器   軟體 not 軟件
  預設 not 默認     快取 not 緩存     網路 not 網絡       金鑰 not 密鑰
  簽章 not 簽名     權杖 not 令牌     回呼 not 回調       冪等 not 幂等
  飯店 not 酒店     開票 not 出票     票價 not 運價       艙等 not 舱位
  登入 not 登錄     註冊 not 注冊     主控台 not 控制台   幣別 not 幣種
  使用者名稱 not 用戶名   電子郵件 not 郵箱   原始碼 not 源碼
  範例 not 示例     變更紀錄 not 更新日誌   簽核 not 審批
  商旅管理公司 not 差旅管理公司   故障排除 not 故障排查
"""

ZH_HANT = {
    # ---- chrome: nav, footer, meta ----------------------------------------
    "Skip to content": "跳至主要內容",
    "FCG Developer Platform — home": "FCG 開放平台 — 首頁",
    "Developer Platform": "開放平台",
    "Primary": "主導覽",
    "Home": "首頁",
    "App Management": "應用程式管理",
    "API Docs": "介面文件",
    "Skills": "Skills 技能包",
    "AI Assistant": "AI 助理",
    "Language": "語言",
    "Login": "登入",
    "Register": "註冊",
    "Open menu": "開啟選單",
    "Back to platform": "返回平台",
    "The FCG Developer Platform: standardised APIs and flexible SDKs for hotel, flight and travel management resources.":
        "FCG 開放平台：針對飯店、機票與商旅管理資源的標準化介面與彈性 SDK。",
    "Products": "產品",
    "Product use cases": "產品應用情境",
    "Developers": "開發者",
    "Platform": "平台",
    # inside a heading only: the hero h1's second line, which is the
    # same word as the footer column but means the product, not a section
    "h:Platform": "開放平台",
    "Error code reference": "錯誤碼說明",
    "© 2026 Fusion Connect Group Holdings Ltd (BVI). All rights reserved.":
        "© 2026 Fusion Connect Group Holdings Ltd (BVI)。保留一切權利。",
    "ENG · 简体 · 繁體": "ENG · 简体 · 繁體",
    "Section": "章節",

    # ---- page titles and meta descriptions -------------------------------
    "AI Assistant — FCG Developer Platform": "AI 助理 — FCG 開放平台",
    "Ask the FCG Developer Platform AI Assistant about API integration, authentication and order workflows.":
        "關於介面對接、簽章驗證與訂單流程，可直接詢問 FCG 開放平台 AI 助理。",
    "Error Code Reference — FCG Developer Platform": "錯誤碼說明 — FCG 開放平台",
    "Every FCG platform error code, its cause and its resolution, across API, SDK and MCP integration.":
        "FCG 平台所有錯誤碼及其成因與處理方式，涵蓋 API、SDK 與 MCP 三種對接方式。",
    "F-Link Flight API — FCG Developer Platform": "F-Link 機票介面 — FCG 開放平台",
    "All nineteen F-Link flight endpoints: search, ticketing, changes, refunds and reference data.":
        "F-Link 機票介面共 19 個：查詢、開票、改期、退票與基礎資料。",
    "G-Link API Reference — FCG Developer Platform": "G-Link 介面參考 — FCG 開放平台",
    "Every G-Link hotel endpoint with methods, paths and a worked request and response example.":
        "G-Link 飯店介面全集，含請求方法、路徑與完整的請求與回應範例。",
    "G-Link Integration Flow — FCG Developer Platform": "G-Link 對接流程 — FCG 開放平台",
    "The recommended eight-step G-Link hotel API integration flow, search through to cancellation.":
        "G-Link 飯店介面建議的八步對接流程，從查詢到取消訂單。",
    "G-Link Hotel API — FCG Developer Platform": "G-Link 飯店介面 — FCG 開放平台",
    "Mandatory interfaces, static data handling and rate limits for the G-Link hotel API.":
        "G-Link 飯店介面的必接介面、靜態資料處理與流量限制規則。",
    "App Management — FCG Developer Platform": "應用程式管理 — FCG 開放平台",
    "Manage the applications behind an FCG API integration. Each product carries its own credential set.":
        "管理 FCG 介面對接所使用的應用程式。每個產品都有獨立的憑證。",
    "FCG Developer Platform": "FCG 開放平台",
    "A travel-focused open platform for distributors. Standardised APIs and flexible SDKs for hotel, flight and TMC travel resources.":
        "為分銷商打造的旅遊開放平台。以標準化介面與彈性 SDK 提供飯店、機票與 TMC 商旅資源。",
    "Sign in — FCG Developer Platform": "登入 — FCG 開放平台",
    "Sign in to the FCG Developer Platform console.": "登入 FCG 開放平台主控台。",
    "Register — FCG Developer Platform": "註冊 — FCG 開放平台",
    "Register a company account for free sandbox access to the FCG Developer Platform.":
        "註冊企業帳號，免費取得 FCG 開放平台沙箱環境。",
    "SDK Integration Centre — FCG Developer Platform": "SDK 整合中心 — FCG 開放平台",
    "Go, Java and Python SDKs for the FCG travel APIs, with install commands and changelogs.":
        "FCG 旅遊介面的 Go、Java 與 Python SDK，附安裝指令與變更紀錄。",
    "Skills Installation Centre — FCG Developer Platform": "Skills 安裝中心 — FCG 開放平台",
    "Official integration skill packages for AI coding assistants, one per FCG travel API.":
        "針對 AI 程式助理的官方對接技能包，每個 FCG 旅遊介面各一個。",

    # ---- AI assistant -----------------------------------------------------
    "Technical support · Integration consulting": "技術支援 · 對接諮詢",
    "Online": "線上",
    "Running into an integration issue?": "對接過程中遇到問題？",
    "Ask directly and get an answer with code examples in seconds, grounded in the platform's own API documentation.":
        "直接提問，數秒內取得以平台介面文件為依據的回答與程式範例。",
    "Start a conversation": "開始對話",
    "FCG Developer Platform AI Assistant": "FCG 開放平台 AI 助理",
    "Hello. I am the FCG Developer Platform AI Assistant. I can help with API integration, signature authentication, order workflows and more.":
        "您好，我是 FCG 開放平台 AI 助理。我可以協助處理介面對接、簽章驗證、訂單流程等問題。",
    "Type a question, or pick one of the common questions to start.":
        "直接輸入問題，或從常見問題中挑一個開始。",
    "How do I generate a request signature?": "如何產生請求簽章？",
    "Sign with your AppSecret using the algorithm in the signing guide, then send the signature with the request. If verification fails you will get":
        "請依簽章指南中的演算法，使用 AppSecret 產生簽章，並隨請求一併送出。若驗證失敗，將回傳",
    "— the usual cause is a wrong AppSecret or a mismatched algorithm.":
        "——常見原因是 AppSecret 有誤或簽章演算法不一致。",
    "Keep the AppSecret on your server. Never ship it to a client.":
        "AppSecret 必須保存在伺服器端，切勿下發到用戶端。",
    "Your question": "您的問題",
    "Ask about authentication, booking flow, error codes…": "可詢問簽章驗證、下單流程、錯誤碼……",
    "Send": "送出",
    "AI responses are for reference only. For professional support,": "AI 回答僅供參考。如需專業支援，請",
    "submit a ticket": "提交工單",
    "and contact the technical team.": "並聯繫技術團隊。",
    "Common questions": "常見問題",
    "Why does availabilityCheck return not bookable?": "availabilityCheck 為什麼回傳無法預訂？",
    "What is the production rate limit?": "生產環境的流量限制是多少？",
    "How should I handle a duplicate orderStatus push?": "orderStatus 重複推送該如何處理？",
    "Which SDK covers the TMC API?": "哪一個 SDK 支援 TMC 介面？",
    "What does SUPPLIER_BIZ_ERROR mean?": "SUPPLIER_BIZ_ERROR 代表什麼？",
    "If the assistant cannot resolve it": "若助理無法解決",
    "Three routes to a human.": "三種轉接真人的方式。",
    "Submit a ticket": "提交工單",
    "Technical support": "技術支援",
    "Include the": "請附上失敗呼叫的",
    "and": "與",
    "from the failing call. Support cannot trace a failure without them.":
        "。缺少這兩個值，技術支援無法追查問題。",
    "Open the console": "開啟主控台",
    "Read the docs": "查閱文件",
    "Docs centre": "文件中心",
    "Interface lists, request and response shapes, worked examples and the full error code table.":
        "介面清單、請求與回應結構、完整範例，以及全部錯誤碼表。",
    "Business consultation": "業務諮詢",
    "Commercial": "業務",
    "Custom solutions, dedicated pricing and TMC API deployment go to the business team, not to support.":
        "客製方案、專屬報價與 TMC 介面部署請洽業務團隊，而非技術支援。",
    "Book a demo": "預約示範",
    "Ask the AI Assistant": "詢問 AI 助理",

    # ---- error codes ------------------------------------------------------
    "All products, all integration methods": "涵蓋所有產品與對接方式",
    "Error Code Reference": "錯誤碼說明",
    "Every error code the platform returns": "平台回傳的每一個錯誤碼",
    ", what causes it and what to do about it. Codes are stable across products; the product and integration columns say where each one can appear.":
        "，以及成因與處理方式。錯誤碼在各產品間保持一致；產品與對接方式兩欄說明它可能出現在何處。",
    "Integration flow": "對接流程",
    "API reference": "介面參考",
    "Error codes": "錯誤碼",
    "Product docs": "產品文件",
    "G-Link sections": "G-Link 章節",
    "Developer tools": "開發者工具",
    "SDK downloads": "SDK 下載",
    "Skills packages": "Skills 技能包",
    "Twelve codes,": "十二個錯誤碼，",
    "four families.": "四個類別。",
    "Platform errors in the": "平台層錯誤碼",
    "range apply everywhere. Product errors are scoped to G-Link or F-Link.":
        "區間在所有情境下皆適用。產品層錯誤碼僅限 G-Link 或 F-Link。",
    "prefixes are integration-layer failures and never reach the travel supplier.":
        "前綴屬於對接層失敗，請求不會送達旅遊供應商。",
    "Code": "錯誤碼",
    "Message": "提示訊息",
    "Product": "產品",
    "Integration": "對接方式",
    "Reason": "成因",
    "Resolution": "處理方式",
    "Signature verification failed": "簽章驗證失敗",
    "AppSecret is incorrect, or the signing algorithm does not match.": "AppSecret 有誤，或簽章演算法不一致。",
    "Check the AppSecret and regenerate the signature using the signing guide.":
        "請核對 AppSecret，並依簽章指南重新產生簽章。",
    "AppKey does not exist or is disabled": "AppKey 不存在或已停用",
    "Application status is abnormal.": "應用程式狀態異常。",
    "Sign in to the console and check the application status. Contact support if it is disabled.":
        "請登入主控台查看應用程式狀態；若已停用，請聯繫技術支援。",
    "Request rate limit exceeded": "請求超出流量限制",
    "Call frequency exceeded the limit.": "呼叫頻率超出上限。",
    "Reduce call frequency and cache locally. Production defaults to 100 requests per minute.":
        "請降低呼叫頻率並在本機快取。生產環境預設每分鐘 100 次。",
    "Invalid city code": "城市代碼無效",
    "The cityCode is not in the supported list.": "cityCode 不在支援清單內。",
    "Use a standard city code from the G-Link city code table.": "請使用 G-Link 城市代碼表中的標準代碼。",
    "Invalid date format": "日期格式無效",
    "The date does not follow YYYY-MM-DD.": "日期未依 YYYY-MM-DD 格式。",
    "Send dates as YYYY-MM-DD, for example 2026-04-01.": "請以 YYYY-MM-DD 傳入日期，例如 2026-04-01。",
    "Hotel is not bookable": "飯店無法預訂",
    "The selected hotel or room type is temporarily unavailable.": "所選飯店或房型暫時無法販售。",
    "Choose another room type, or contact support to confirm the hotel status.":
        "請改選房型，或聯繫技術支援確認飯店狀態。",
    "Flight is fully booked": "航班已客滿",
    "No economy seats remain on the selected flight.": "所選航班經濟艙已無空位。",
    "Search for another flight or cabin.": "請查詢其他航班或艙等。",
    "Change request is too late": "改期申請過晚",
    "Departure is less than four hours away.": "距起飛不足四小時。",
    "Submit changes earlier, or contact support for manual handling.":
        "請提早提交改期，或聯繫技術支援人工處理。",
    "MCP connection timed out": "MCP 連線逾時",
    "Network is unstable, or the server is busy.": "網路不穩定，或伺服器忙碌。",
    "Check the network, raise the timeout to 30 seconds and add retry handling.":
        "請檢查網路，將逾時時間調整為 30 秒並加入重試機制。",
    "MCP authentication failed": "MCP 驗證失敗",
    "Token has expired or has an invalid format.": "權杖已過期或格式不正確。",
    "Get a new token and pass it in the Authorization header as a Bearer token.":
        "請重新取得權杖，並以 Bearer 形式放入 Authorization 標頭。",
    "SDK initialisation failed": "SDK 初始化失敗",
    "AppKey or AppSecret is empty or malformed.": "AppKey 或 AppSecret 為空或格式不正確。",
    "Check the initialisation parameters and confirm both values are supplied.":
        "請檢查初始化參數，確認兩個值均已正確傳入。",
    "SDK version is incompatible": "SDK 版本不相容",
    "The SDK version is too old for this capability.": "目前 SDK 版本過舊，不支援此功能。",
    "Upgrade to the latest SDK and review the changelog.": "請升級至最新 SDK，並查閱變更紀錄。",
    "HTTP 200 is not success.": "HTTP 200 並不代表成功。",
    "Read the": "請讀取回應內容中的",
    "field in the response body. A supplier business failure returns HTTP 200 with":
        "欄位。供應商業務失敗同樣回傳 HTTP 200，並帶有",
    ", and the codes above appear the same way.": "，上表中的錯誤碼也以同樣方式回傳。",
    "What to log": "需要記錄的資訊",
    "Keep": "請保留",
    "against every call. Support cannot trace a failure without them.":
        "，每次呼叫都要記錄。缺少這兩個值，技術支援無法追查問題。",
    "where it is returned — it identifies the call at the supplier, not at the platform.":
        "（介面回傳此欄位時）——它標示的是供應商端的呼叫，而非平台端。",
    "Record the request timestamp in UTC. Rate-limit disputes are settled on the platform's clock.":
        "請以 UTC 記錄請求時間。流量限制爭議以平台時鐘為準。",

    # ---- F-Link -----------------------------------------------------------
    "Direct airline seat inventory": "航空公司直連艙位庫存",
    "Direct airline seat inventory.": "航空公司直連艙位庫存。",
    "Domestic and international carriers with BSP support, covering search, pricing, ticketing, refunds and changes. Nineteen endpoints, one path pattern.":
        "涵蓋國內與國際航空公司並支援 BSP，包含查詢、定價、開票、退票與改期。19 個介面，統一的路徑規則。",
    "Download SDK": "下載 SDK",
    "All F-Link endpoints.": "F-Link 全部介面。",
    "Every flight path carries a": "每個機票介面路徑都包含",
    "segment —": "區段——",
    "or": "或",
    "— which sets the language of returned labels and error messages. The translation endpoint is the one exception and takes no language segment.":
        "——用於指定回傳文字與錯誤訊息的語言。僅欄位翻譯介面例外，不帶語言區段。",
    "No.": "編號",
    "Interface": "介面",
    "Method": "方法",
    "Path": "路徑",
    "Flight search": "航班查詢",
    "Get more fare quotes": "取得更多票價",
    "Pre-booking price verification": "下單前驗價",
    "Submit pre-booking order": "提交預訂單",
    "Order payment": "訂單付款",
    "Standard order details": "標準訂單明細",
    "Cancel standard order": "取消標準訂單",
    "Change flight search": "改期航班查詢",
    "Submit change request": "提交改期申請",
    "Cancel change request": "取消改期申請",
    "Change request details": "改期申請明細",
    "Submit refund request": "提交退票申請",
    "Refund request details": "退票申請明細",
    "Confirm or cancel refund": "確認或取消退票",
    "Query airport information": "查詢機場資訊",
    "Query airline information": "查詢航空公司資訊",
    "Search airport information": "搜尋機場資訊",
    "Query nationality list": "查詢國籍清單",
    "Query translation information": "查詢欄位翻譯",
    "How the set divides": "介面分組",
    "Search and price": "查詢與定價",
    ". Verify before booking; fares move.": "。下單前務必驗價，票價會變動。",
    "Book and ticket": "下單與開票",
    "Change": "改期",
    "— four endpoints, from change search through to change detail. Changes inside four hours of departure are rejected and need manual handling.":
        "——四個介面，從改期查詢到改期明細。距起飛不足四小時的改期會被拒絕，需人工處理。",
    "Refund": "退票",
    "— apply, detail, then confirm or cancel.": "——申請、明細，再確認或取消。",
    "Reference data": "基礎資料",
    "— airports, airlines, airport search, nationality list and field translations. Cache these locally.":
        "——機場、航空公司、機場搜尋、國籍清單與欄位翻譯。請在本機快取。",
    "Verify immediately before order creation.": "下單前請立即驗價。",
    "returns the current price and confirms the fare is still bookable. Skipping it is the most common cause of a failed":
        "會回傳目前價格並確認該票價仍可預訂。略過這一步是下單失敗最常見的原因",
    "Install the F-Link Skills package": "安裝 F-Link Skills 技能包",

    # ---- G-Link API reference --------------------------------------------
    "Sandbox and production": "沙箱與生產環境",
    "G-Link API Reference": "G-Link 介面參考",
    "Every G-Link endpoint, grouped by what it does.": "G-Link 全部介面，依功能分組。",
    "One is expanded in full below as the worked example; the request and response shape is consistent across the set.":
        "下方以其中一個介面作為完整範例；整套介面的請求與回應結構一致。",
    "Twenty endpoints,": "二十個介面，",
    "five groups.": "五個分組。",
    "Static data first, then live booking, then orders and callbacks. Paths are shown against the production host; the sandbox host is issued with sandbox credentials.":
        "先是靜態資料，接著即時預訂，最後是訂單與回呼。路徑以生產環境網域為準；沙箱網域會隨沙箱憑證一併提供。",
    "Regional static information": "地區靜態資料",
    "Query country list": "查詢國家清單",
    "Query city list": "查詢城市清單",
    "Query popular city list": "查詢熱門城市清單",
    "Query business district list": "查詢商圈清單",
    "Query administrative district list": "查詢行政區清單",
    "Hotel information": "飯店資訊",
    "Available hotel ID list": "可販售飯店 ID 清單",
    "Query hotel basic information": "查詢飯店基本資訊",
    "Hotel daily lowest price": "飯店每日最低價",
    "Hotel static information increment": "飯店靜態資料增量",
    "Hotel booking": "飯店預訂",
    "Hotel real-time product query": "飯店即時商品查詢",
    "Trial booking (availability check)": "試單（可訂性檢查）",
    "Create order": "建立訂單",
    "Order information": "訂單資訊",
    "Order detail query": "訂單明細查詢",
    "Cancel order": "取消訂單",
    "Callback notification": "回呼通知",
    "Order status push": "訂單狀態推送",
    "Worked example — query country list": "完整範例——查詢國家清單",
    "Interface description": "介面說明",
    "Caller": "呼叫方",
    "Partner": "合作夥伴",
    "Responder": "回應方",
    "Rate limit": "流量限制",
    "Partners call this endpoint to query the country list held in the FCG system, normally once, as part of building local reference data.":
        "合作夥伴呼叫此介面查詢 FCG 系統中的國家清單，通常在建立本機基礎資料時呼叫一次。",
    "Body parameters": "請求內容參數",
    "Optional": "選填",
    "Language.": "語言。",
    "for Chinese,": "為中文，",
    "for English. Defaults to English.": "為英文。預設為英文。",
    "Response structure": "回應結構",
    "Required": "必填",
    "Platform business code.": "平台業務代碼。",
    "indicates success. A supplier business failure can still return HTTP 200 with":
        "表示成功。供應商業務失敗仍可能回傳 HTTP 200，並帶有",
    "Country list.": "國家清單。",
    "Country code.": "國家代碼。",
    "Country ID.": "國家 ID。",
    "Country name.": "國家名稱。",
    "G-Link downstream request ID. Usually returned after a successful call.":
        "G-Link 下游請求 ID。通常在呼叫成功後回傳。",
    "Platform message. Typically": "平台提示訊息。成功時通常為",
    "on success.": "。",
    "Platform request ID.": "平台請求 ID。",
    "Platform trace ID.": "平台追蹤 ID。",
    "Request": "請求",
    "Response": "回應",
    "Read": "請判讀",
    ", not the HTTP status.": "，而非 HTTP 狀態碼。",
    "A supplier business failure returns HTTP 200 with": "供應商業務失敗會回傳 HTTP 200，並帶有",
    ". Branch on the body.": "。請依回應內容分支處理。",
    "Use an SDK instead": "改用 SDK 對接",

    # ---- G-Link integration flow -----------------------------------------
    "Recommended integration flow": "建議對接流程",
    "G-Link Integration Flow": "G-Link 對接流程",
    "The order in which to wire the G-Link hotel API.": "G-Link 飯店介面的對接順序。",
    "Eight steps, search through to cancellation, each one a single endpoint.":
        "八個步驟，從查詢到取消訂單，每一步對應一個介面。",
    "Standard API integration,": "標準介面對接，",
    "in order.": "依序進行。",
    "Follow the sequence. Steps one and two build local reference data and run on a schedule; steps three onwards are live and run per booking.":
        "請依順序對接。第一、二步用於建立本機基礎資料，以排程執行；第三步起為即時呼叫，每筆預訂觸發一次。",
    "Step 01": "步驟 01", "Step 02": "步驟 02", "Step 03": "步驟 03", "Step 04": "步驟 04",
    "Step 05": "步驟 05", "Step 06": "步驟 06", "Step 07": "步驟 07", "Step 08": "步驟 08",
    "Query all available hotel IDs": "查詢所有可販售飯店 ID",
    "Query hotel static information by hotel ID": "依飯店 ID 查詢靜態資訊",
    "Real-time query of sales information and lowest price": "即時查詢販售資訊與最低價",
    "Check the rate plan is bookable and return the latest price": "檢查價格方案可訂性並回傳最新價格",
    "Create the order once trial booking succeeds": "試單成功後建立訂單",
    "Take payment after order creation": "訂單建立後完成付款",
    "Query order details": "查詢訂單明細",
    "Cancel the order as needed": "視需要取消訂單",
    "What runs on a schedule, and what runs live": "哪些以排程執行，哪些即時呼叫",
    "Scheduled.": "排程執行。",
    "Hotel ID list, hotel and room-type static information, country and city reference data, and the":
        "飯店 ID 清單、飯店與房型靜態資訊、國家與城市基礎資料，以及",
    "change feed. Cache all of it locally.": "變更訂閱。以上全部請在本機快取。",
    "Live.": "即時呼叫。",
    "Product details, trial booking, order creation, payment, cancellation and order detail. These are called per traveller action and count against the rate limit.":
        "商品明細、試單、建立訂單、付款、取消與訂單明細。這些介面隨旅客操作觸發，並計入流量限制額度。",
    "Idempotent.": "冪等處理。",
    "The order status push,": "訂單狀態推送",
    ", may be delivered more than once. Handle repeats without creating duplicate state.":
        "可能被送達多次。請做好去重，避免產生重複狀態。",
    "Trial booking twice.": "試單執行兩次。",
    "Run": "請在呼叫",
    "again immediately before": "之前，立即再執行一次",
    ". Inventory and price can move between the customer's decision and the order call.":
        "。從客人決定下單到實際呼叫下單介面之間，庫存與價格都可能變動。",
    "Open the API reference": "開啟介面參考",
    "Install the G-Link Skills package": "安裝 G-Link Skills 技能包",

    # ---- G-Link overview --------------------------------------------------
    "Supports both SDK and API integration": "同時支援 SDK 與 API 對接",
    "Major global hotel inventory": "全球主要飯店庫存",
    "over one standardised interface. The full workflow runs from real-time search and trial booking through to reservation, payment and cancellation.":
        "，透過一套標準化介面提供。完整流程涵蓋即時查詢、試單、預訂、付款與取消。",
    "Eight interfaces carry a complete hotel booking.": "八個介面即可完成一筆飯店預訂。",
    "These are the mandatory endpoints. Everything else in the reference is static data, incremental updates or callback handling built around them.":
        "以下為必接介面。介面參考中的其餘部分，都是圍繞這些介面的靜態資料、增量更新與回呼處理。",
    "Mandatory interfaces, and when to call them": "必接介面及其呼叫時機",
    ". Queries the lowest price for mapped hotels, as the reference for whether a hotel appears in a local hotel list.":
        "。查詢已對應飯店的最低價，作為該飯店是否顯示在本機飯店清單中的依據。",
    ". Called in real time when a customer enters the hotel detail or booking path.":
        "。客人進入飯店明細頁或預訂流程時即時呼叫。",
    "Trial booking": "試單",
    ". Validates that a bookable product can be reserved, passing the actual number of rooms.":
        "。檢查可販售商品是否真的可訂，需傳入實際預訂間數。",
    ". Called once trial booking passes and the local order is created. Run trial booking again immediately before this call.":
        "。試單通過且本機訂單建立成功後呼叫。呼叫前請再執行一次試單檢查。",
    ". Called after the local customer pays, or when an order needs confirmation, to notify the service team to process it.":
        "。本機客人付款成功後，或訂單需要確認時呼叫，用於通知服務團隊處理該訂單。",
    ". Called when an order is unpaid for 30 minutes, or the customer cancels. A success response means polling should stop.":
        "。訂單超過 30 分鐘未付款，或客人主動取消時呼叫。回傳成功即應停止輪詢。",
    ". After payment notification, the service team processes the order and pushes status. This interface must be idempotent.":
        "。收到付款通知後，服務團隊處理訂單並推送狀態。此介面必須實作冪等。",
    ". Compensation only, if no confirmation arrives after payment. Frequent polling is unnecessary; stop once the order is confirmed or cancelled.":
        "。僅作為補償機制，用於付款後未收到確認結果的情況。不需頻繁輪詢；訂單確認或取消後即應停止。",
    "Static data and incremental updates": "靜態資料與增量更新",
    "Pull the available hotel list from": "透過",
    ", then take hotel and room-type detail from": "取得可販售飯店清單，再透過",
    "supply country and city reference data, normally used to build foundational data and map against the FCG hotel system.":
        "提供國家與城市基礎資料，通常用於建立基礎資料並與 FCG 飯店系統進行對應。",
    "Call": "請定期呼叫",
    "periodically for the list of hotel IDs whose static information has changed — additions, modifications and deletions — then resynchronise the affected records rather than re-pulling the full set.":
        "，取得靜態資訊有變動的飯店 ID 清單——包含新增、修改與刪除——然後只同步受影響的紀錄，不需全量重新拉取。",
    "Rate limits.": "流量限制說明。",
    "Production defaults to 100 requests per minute per application. Cache static data locally and reserve live calls for search, trial booking and order operations.":
        "生產環境預設每個應用程式每分鐘 100 次。請在本機快取靜態資料，把即時呼叫留給查詢、試單與訂單操作。",
    "Read the integration flow": "查看對接流程",
    "Full API reference": "完整介面參考",

    # ---- app management ---------------------------------------------------
    "Independent credentials per product": "每個產品獨立憑證",
    "Manage the applications behind an API integration.": "管理介面對接所使用的應用程式。",
    "Each product carries its own credential set, so a hotel key never unlocks a flight endpoint and a sandbox key never reaches production.":
        "每個產品都有獨立的憑證，因此飯店金鑰無法呼叫機票介面，沙箱金鑰也不會觸及生產環境。",
    "Create an application": "建立應用程式",
    "Sign in to the console": "登入主控台",
    "Applications": "應用程式",
    "Three applications,": "三個應用程式，",
    "three credential sets.": "三套獨立憑證。",
    "Credentials are shown in the console once signed in. Nothing on this page reveals a live key.":
        "登入後可在主控台查看憑證。本頁不會顯示任何真實金鑰。",
    "Hotel search, booking, payment and cancellation workflows.": "飯店查詢、預訂、付款與取消流程。",
    "App key": "AppKey",
    "App secret": "AppSecret",
    "Created": "建立時間",
    "28 April 2026": "2026 年 4 月 28 日",
    "Environment": "環境",
    "Sandbox": "沙箱",
    "View credentials": "查看憑證",
    "Flight search, ticketing, refunds and changes.": "航班查詢、開票、退票與改期。",
    "Rapid deployment of corporate travel platforms.": "快速建置企業商旅平台。",
    "The TMC API sandbox supports USD only.": "TMC 介面沙箱僅支援美元結算。",
    "Application example": "應用範例",
    "Traveller-facing client homepage.": "面向旅客的前台首頁。",
    "A complete client example wired to G-Link hotel and F-Link flight real-time inventory. Open it, read it, then take the source and start building.":
        "一個已接上 G-Link 飯店與 F-Link 機票即時庫存的完整前台範例。開啟、閱讀，然後取走原始碼開始開發。",
    "Inventory": "庫存",
    "F-Link, live": "F-Link 即時",
    "Source": "原始碼",
    "Available on request": "可申請取得",
    "Open full client": "開啟完整範例",
    "Download source": "下載原始碼",
    "Environments": "環境",
    "Sandbox first, production by volume.": "先用沙箱，生產按量計費。",
    "Test the full API set in sandbox at no upfront cost. Production keys are issued once integration testing passes, and billed on usage with no minimum spend.":
        "在沙箱中免費測試全部介面，無前期費用。對接測試通過後即可取得生產金鑰，按呼叫量計費，無最低消費。",
    "Open on registration": "註冊即開通",
    "Production rate limit": "生產環境流量限制",
    "Billing": "計費方式",
    "Usage-based": "按量計費",
    "Register for free": "免費註冊",

    # ---- homepage ---------------------------------------------------------
    "FCG Developer": "FCG",
    "A travel-focused open platform for distributors": "為分銷商打造的旅遊開放平台",
    "such as OTAs and travel management companies. Standardised APIs and flexible SDKs aggregate and distribute hotel, flight and other core travel resources, plus TMC API capabilities, so partners can launch branded travel platforms faster.":
        "，服務 OTA 與商旅管理公司等客戶。以標準化介面與彈性 SDK 彙整並分銷飯店、機票等核心旅遊資源，並提供 TMC 介面能力，協助合作夥伴更快推出自有品牌的旅遊平台。",
    "Start Integration": "開始對接",
    "Book a Demo": "預約示範",
    "core products": "核心產品",
    "Go · Java · Python": "Go · Java · Python",
    "smart integration": "智慧對接",
    "Sandbox request": "沙箱請求",
    "shell": "shell",
    "Illustrative fragment only. Placeholders in braces stand in for real values, and the authoritative request and response contracts live in the API Docs.":
        "此處僅為示意片段。大括號中的佔位符代表實際值，正式的請求與回應規格請以介面文件為準。",
    "Core products": "核心產品",
    "Three Core Products,": "三大核心產品，",
    "One Integration Surface.": "一套對接介面。",
    "Three core products cover the key travel workflows end to end. Compare them row by row, then start with the one your stack needs first.":
        "三大核心產品端到端涵蓋關鍵旅遊業務流程。逐列比較，再從你的系統最先需要的那一個開始。",
    "Hotel API": "飯店介面",
    "Major global hotel inventory with industry-grade data accuracy.": "全球主要飯店庫存，業界級資料準確度。",
    "Coverage": "涵蓋範圍",
    "Major global hotel inventory, with the full workflow from real-time search and test booking through to reservation and cancellation.":
        "全球主要飯店庫存，完整流程涵蓋即時查詢、試單、預訂與取消。",
    "Workflow": "業務流程",
    "search": "查詢",
    "test booking": "試單",
    "reserve": "預訂",
    "cancel": "取消",
    "Integration surface": "對接介面",
    "Illustrative shape, not a published signature.": "僅為結構示意，非正式介面規格。",
    "Capabilities": "能力",
    "Search APIs": "查詢介面",
    "Booking management": "預訂管理",
    "Rate calendar": "價格日曆",
    "Room details": "房型明細",
    "Start with G-Link": "從 G-Link 開始",
    "Flight API": "機票介面",
    "Direct airline seat inventory across domestic and international carriers.": "涵蓋國內與國際航空公司的直連艙位庫存。",
    "Direct airline seat inventory for domestic and international carriers, with BSP support, covering search, pricing, ticketing, refunds and changes.":
        "涵蓋國內與國際航空公司的直連艙位庫存，支援 BSP，包含查詢、定價、開票、退票與改期。",
    "price": "定價",
    "ticket": "開票",
    "refund / change": "退改",
    "Live fares": "即時票價",
    "Order management": "訂單管理",
    "Refund rules": "退改規則",
    "Start with F-Link": "從 F-Link 開始",
    "Travel Management API": "商旅管理介面",
    "A mature, API-based travel management layer for enterprise programmes.": "為企業商旅專案打造的成熟介面化商旅管理層。",
    "Mature API-based travel management. Launch a branded enterprise travel service quickly, with deep customisation and no need to build from scratch.":
        "成熟的介面化商旅管理能力。快速推出自有品牌的企業商旅服務，支援深度客製，不需從零建置。",
    "policy": "商旅政策",
    "approval": "簽核",
    "expense": "費用",
    "billing": "結算",
    "Enterprise control": "企業控管",
    "Expense rules": "費用規則",
    "Billing reports": "結算報表",
    "Approval flow": "簽核流程",
    "Start with TMC API": "從 TMC 介面開始",
    "New": "新",
    "Integration Skills for AI Coding Assistants.": "為 AI 程式助理打造的對接技能包。",
    "Integration skill packages for AI coding assistants.": "為 AI 程式助理打造的對接技能包。",
    "Import them into Claude, ChatGPT or Copilot for more accurate authentication code, API debugging and issue diagnosis.":
        "匯入 Claude、ChatGPT 或 Copilot，取得更準確的驗證程式碼、介面除錯與問題診斷。",
    "Full G-Link and F-Link coverage": "完整涵蓋 G-Link 與 F-Link",
    "Authentication, query, booking and payment flows": "驗證、查詢、預訂與付款流程",
    "Prompt templates included": "內建提示詞範本",
    "Continuously updated": "持續更新",
    "Browse Skills": "瀏覽技能包",
    "Package layout": "技能包結構",
    "Where Each Product Is Used.": "各產品的典型應用情境。",
    "Three products, nine established patterns.": "三個產品，九種成熟模式。",
    "Match the pattern closest to your own before you scope the integration.":
        "在評估對接範圍前，先找到與你最接近的那一種。",
    "Hotel API Distribution": "飯店介面分銷",
    "OTA aggregation": "OTA 彙整",
    "Enterprise travel procurement": "企業商旅採購",
    "Destination management": "目的地管理",
    "Flight API Distribution": "機票介面分銷",
    "Agency distribution": "代理商分銷",
    "Travel policy control": "商旅政策控管",
    "Fare aggregation and comparison": "票價彙整比價",
    "Branded deployment": "品牌化部署",
    "Enterprise policy controls": "企業政策控管",
    "Unified billing and reporting": "統一結算與報表",
    "Flexible integration options": "彈性的對接方式",
    "Integrate the Way Your Stack Works.": "依你的技術架構方式對接。",
    "Three routes onto the same capabilities.": "三條路徑，通往同一套能力。",
    "Pick the one that matches how your team already builds.": "選擇最符合團隊現有開發方式的那一條。",
    "MCP Smart Integration": "MCP 智慧對接",
    "Exposes travel capabilities over the Model Context Protocol so AI models can call them directly. Built for LLM applications and assistants.":
        "透過 Model Context Protocol 開放旅遊能力，讓 AI 模型直接呼叫。為大型語言模型應用與助理而設計。",
    "Tool calling": "工具呼叫",
    "Fast SDK Integration": "SDK 快速對接",
    "Typed clients": "具型別的用戶端",
    "Authentication, retry and serialisation are built in, so a working call is a few lines rather than a project. Go, Java and Python are available today.":
        "內建驗證、重試與序列化，幾行程式碼即可完成一次可用呼叫，不必另開專案。目前提供 Go、Java 與 Python。",
    "Node.js — in progress": "Node.js — 開發中",
    "Language agnostic": "不限語言",
    "Standard APIs callable from any language or framework. Use them when you would rather own the client layer yourself.":
        "標準介面，任何語言或框架都能呼叫。適合希望自行掌控用戶端層的團隊。",
    "Any framework": "不限框架",
    "Customer types": "客戶類型",
    "Find the Right Integration Path.": "找到適合你的對接路徑。",
    "Three profiles, three recommended routes.": "三類客戶，三條建議路徑。",
    "Read across your own row and start there.": "找到你所屬的那一列，從那裡開始。",
    "Who you are": "你是誰",
    "What you are solving": "你要解決什麼",
    "Recommended path": "建議路徑",
    "Distributors / OTAs": "分銷商 / OTA",
    "Aggregating hotel and flight supply for onward distribution.": "彙整飯店與機票供給並對外分銷。",
    "Start integration for distributors and OTAs": "分銷商與 OTA 開始對接",
    "Start": "開始",
    "Travel Management Companies": "商旅管理公司",
    "Most popular": "最受歡迎",
    "Running managed travel programmes across hotel, flight and policy in one place.":
        "在同一個平台統一管理飯店、機票與商旅政策。",
    "Full product suite": "全產品線",
    "API integration": "介面對接",
    "Start integration for travel management companies": "商旅管理公司開始對接",
    "Large Enterprises": "大型企業",
    "Standing up a branded corporate travel service without building it from scratch.":
        "在不需從零建置的前提下，推出自有品牌的企業商旅服務。",
    "Fast TMC API deployment": "TMC 介面快速部署",
    "Start integration for large enterprises": "大型企業開始對接",
    "Platform statistics": "平台數據",
    "Enterprise clients": "企業客戶",
    "Daily requests": "每日請求",
    "Service uptime": "服務可用率",
    "Partner network": "合作網路",
    "The Supply and Partner Network Behind FCG.": "FCG 背後的供給與合作網路。",
    "Trusted by 50+ enterprise clients": "已服務 50 餘家企業客戶",
    ", including central state-owned enterprises and Fortune Global 500 companies such as State Grid, China Mobile and Ping An.":
        "，其中包括國家電網、中國移動、平安等中央企業與《財星》全球 500 大企業。",
    "Get started": "開始使用",
    "Two Ways to Begin.": "兩種開始方式。",
    "Test the platform yourself": "自行測試平台",
    ", or bring in the business team for a custom deployment.": "，或洽業務團隊進行客製化部署。",
    "Free access": "免費接入",
    "Register for a Sandbox.": "註冊沙箱環境。",
    "Register for a sandbox and test the full API set at no upfront cost. Production usage is billed by volume.":
        "註冊沙箱即可免費測試全部介面，無前期費用。生產環境按呼叫量計費。",
    "Full sandbox experience": "完整沙箱體驗",
    "Complete API docs and SDKs": "完整介面文件與 SDK",
    "Community support and docs centre": "社群支援與文件中心",
    "Usage-based billing with no minimum spend": "按量計費，無最低消費",
    "Talk to the Business Team.": "洽詢業務團隊。",
    "Discuss custom solutions, dedicated pricing and TMC API deployment with the business team.":
        "與業務團隊討論客製方案、專屬報價與 TMC 介面部署。",
    "Dedicated business manager": "專屬業務經理",
    "Custom integration plan": "客製對接方案",
    "TMC API deployment demo": "TMC 介面部署示範",
    "Dedicated SLA coverage": "專屬 SLA 保障",
    "Book a 30-minute demo": "預約 30 分鐘示範",

    # ---- auth -------------------------------------------------------------
    "Developer console": "開發者主控台",
    "Travel API integration in one place.": "旅遊介面對接，一站完成。",
    "Built for distributors and travel management companies, with full hotel and flight API coverage and support for both SDK and REST integration.":
        "為分銷商與商旅管理公司打造，完整涵蓋飯店與機票介面，同時支援 SDK 與 REST 兩種對接方式。",
    "Partners": "合作夥伴",
    "Uptime": "可用率",
    "Welcome back": "歡迎回來",
    "Sign in to access your developer console.": "登入以進入開發者主控台。",
    "Continue with Google": "使用 Google 繼續",
    "Or use your account": "或使用帳號登入",
    "Account": "帳號",
    "Username or email": "使用者名稱或電子郵件",
    "Password": "密碼",
    "Forgotten your password?": "忘記密碼？",
    "Sign in": "登入",
    "No account yet?": "還沒有帳號？",
    "Register once,": "註冊一次，",
    "test everything.": "測試全部介面。",
    "Set up a company account and complete the onboarding details to reach the platform console. The sandbox opens immediately and costs nothing upfront.":
        "建立企業帳號並填妥進件資訊，即可進入平台主控台。沙箱環境即時開通，無前期費用。",
    "Instant sandbox access": "即時開通沙箱",
    "Full API documentation access": "完整介面文件權限",
    "Technical ticket support": "技術工單支援",
    "TMC API application eligibility": "TMC 介面申請資格",
    "Create your account": "建立帳號",
    "Set up your company account and complete the onboarding details to access the platform console.":
        "建立企業帳號並填妥進件資訊，即可存取平台主控台。",
    "Sign up with Google": "使用 Google 註冊",
    "Or register with your details": "或填寫資料註冊",
    "Username": "使用者名稱",
    "Company name": "企業名稱",
    "Contact person": "聯絡人",
    "Phone number": "聯絡電話",
    "Email": "電子郵件",
    "Settlement currency": "結算幣別",
    "CNY — Chinese Yuan": "CNY — 人民幣",
    "USD — US Dollar": "USD — 美元",
    "Create account": "建立帳號",
    "The TMC API sandbox supports USD only. Settlement currency can be changed later from the console.":
        "TMC 介面沙箱僅支援美元結算。結算幣別可稍後在主控台修改。",
    "Already registered?": "已有帳號？",

    # ---- SDK --------------------------------------------------------------
    "Auth, retry and serialisation built in": "內建驗證、重試與序列化",
    "SDK Integration Centre": "SDK 整合中心",
    "Multilingual SDKs": "多語言 SDK",
    "with install commands, example code, changelogs and security verification. Go, Java and Python are published today; Node.js is in progress.":
        "，附安裝指令、範例程式、變更紀錄與簽章驗證工具。目前已發布 Go、Java 與 Python，Node.js 開發中。",
    "Get sandbox credentials": "取得沙箱憑證",
    "Published SDK releases": "已發布 SDK",
    "Languages · Go · Java · Python": "支援語言 · Go · Java · Python",
    "Core integration coverage": "核心對接涵蓋率",
    "Available now": "現已提供",
    "Install, configure the key pair,": "安裝、設定金鑰對，",
    "call the API.": "即可呼叫介面。",
    "Every SDK ships with the same three things: a quick start, a changelog and a signature verification helper. Download the package, install it, then configure AppKey and AppSecret on your server — never in a client.":
        "每個 SDK 都包含同樣三樣東西：快速上手、變更紀錄與簽章驗證工具。下載並安裝後，在伺服器端設定 AppKey 與 AppSecret——切勿放在用戶端。",
    "TMC API · Java": "TMC 介面 · Java",
    "Published release. Confirm runtime versions from the release notes before installing.":
        "正式發布版本。安裝前請於發布說明中確認執行環境版本需求。",
    "Version": "版本",
    "Released": "發布日期",
    "30 July 2026": "2026 年 7 月 30 日",
    "Status": "狀態",
    "Published": "已發布",
    "Install": "安裝",
    "Copy": "複製",
    "View docs": "查看文件",
    "Download": "下載",
    "TMC API · Python": "TMC 介面 · Python",
    "TMC API · Go": "TMC 介面 · Go",
    "Open Platform Go SDK": "開放平台 Go SDK",
    "G-Link Hotel · Python": "G-Link 飯店 · Python",
    "G-Link Hotel Python SDK": "G-Link 飯店 Python SDK",
    "13 July 2026": "2026 年 7 月 13 日",
    "Node.js is in progress.": "Node.js 開發中。",
    "Until it publishes, call the REST endpoints directly — the": "在發布之前，請直接呼叫 REST 介面——",
    "carries the full request and response shape.": "中提供完整的請求與回應結構。",
    "Integration options": "對接方式",
    "Three ways in.": "三種接入方式。",
    "MCP smart integration": "MCP 智慧對接",
    "Lets an AI model call travel capabilities directly. Built for LLM applications and assistants.":
        "讓 AI 模型直接呼叫旅遊能力。為大型語言模型應用與助理而設計。",
    "Fast SDK integration": "SDK 快速對接",
    "Authentication, retry and serialisation handled for you. Node.js is in progress.":
        "驗證、重試與序列化皆已內建。Node.js 開發中。",
    "Any language": "不限語言",
    "Standard APIs callable from any language or framework. No SDK required.":
        "標準介面，任何語言或框架都能呼叫，不需 SDK。",

    # ---- Skills -----------------------------------------------------------
    "One official package per API": "每個介面一個官方技能包",
    "Skills Installation Centre": "Skills 安裝中心",
    "Import one into Claude, Codex, Cursor, Kiro or Gemini CLI and the assistant writes more accurate authentication code, debugs API calls and diagnoses failures against the real interface.":
        "匯入 Claude、Codex、Cursor、Kiro 或 Gemini CLI 後，助理即可依據真實介面撰寫更準確的驗證程式碼、除錯介面呼叫並診斷故障。",
    "Browse packages": "瀏覽技能包",
    "Official Skills packages": "官方技能包",
    "AI assistant categories": "支援的 AI 助理類別",
    "Packages": "技能包",
    "Install by command,": "指令安裝，",
    "or download the file.": "或下載檔案。",
    "Each package installs remotely with one command, or downloads as a single":
        "每個技能包都可用一行指令遠端安裝，也可下載為單一",
    "you drop into the assistant yourself. Both routes carry the same content.":
        "檔案自行放入助理。兩種方式內容完全相同。",
    "G-Link Hotel API Skills": "G-Link 飯店介面技能包",
    "Full hotel integration flow: auth, search, booking, payment, order management, webhooks and troubleshooting.":
        "完整飯店對接流程：驗證、查詢、預訂、付款、訂單管理、Webhook 與故障排除。",
    "Sandbox ready": "沙箱可用",
    "Production ready": "生產可用",
    "Updated": "更新時間",
    "5 April 2026": "2026 年 4 月 5 日",
    "Remote install": "遠端安裝",
    "View details": "查看詳情",
    "Download SKILL.md": "下載 SKILL.md",
    "F-Link Flight API Skills": "F-Link 機票介面技能包",
    "Full flight integration flow: auth, search, booking, ticketing, change and refund, webhooks and troubleshooting.":
        "完整機票對接流程：驗證、查詢、預訂、開票、退改、Webhook 與故障排除。",
    "Full TMC integration flow: auth, flight and hotel booking, approvals, policy standards, organisation hierarchy, webhooks and troubleshooting.":
        "完整 TMC 對接流程：驗證、機票與飯店預訂、簽核、政策標準、組織架構、Webhook 與故障排除。",
    "How to install": "如何安裝",
    "Two routes,": "兩條路徑，",
    "one outcome.": "同一結果。",
    "Remote install is the shorter path and stays current. The downloadable file suits an assistant with no network access, or a repository that should carry its own copy.":
        "遠端安裝較快，且永遠保持最新。下載檔案較適合沒有網路存取權限的助理，或需要在儲存庫內自帶一份副本的情況。",
    "Run the install command with": "執行安裝指令，並將",
    "set to your assistant.": "設為你所使用的助理。",
    "Or download": "或下載",
    "and place it where your assistant reads skills.": "，放到助理讀取技能包的目錄中。",
    "Packages are updated continuously — reinstall to pick up interface changes.":
        "技能包持續更新——重新安裝即可取得介面變更。",
    "Prompt templates are included. Credentials are not; configure those yourself.":
        "已內建提示詞範本。憑證不包含在內，需自行設定。",
}
