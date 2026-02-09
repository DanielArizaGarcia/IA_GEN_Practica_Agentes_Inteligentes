✅ ADK components imported successfully.
✅ Helper functions defined.
✅ Fee lookup function created
💳 Test: {'status': 'success', 'fee_percentage': 0.02}
✅ Exchange rate function created
💱 Test: {'status': 'success', 'rate': 0.93}
✅ Currency agent created with custom function tools
🔧 Available tools:
  • get_fee_for_payment_method - Looks up company fee structure
  • get_exchange_rate - Gets current exchange rates

 ### Created new session: debug_session_id

User > I want to convert 500 US Dollars to Euros using my Platinum Credit Card. How much will I receive?
[90m[logging_plugin] 🚀 USER MESSAGE RECEIVED[0m
[90m[logging_plugin]    Invocation ID: e-75bfb9bb-1c95-4140-8b12-72055c3a478b[0m
[90m[logging_plugin]    Session ID: debug_session_id[0m
[90m[logging_plugin]    User ID: debug_user_id[0m
[90m[logging_plugin]    App Name: InMemoryRunner[0m
[90m[logging_plugin]    Root Agent: currency_agent[0m
[90m[logging_plugin]    User Content: text: 'I want to convert 500 US Dollars to Euros using my Platinum Credit Card. How much will I receive?'[0m
[90m[logging_plugin] 🏃 INVOCATION STARTING[0m
[90m[logging_plugin]    Invocation ID: e-75bfb9bb-1c95-4140-8b12-72055c3a478b[0m
[90m[logging_plugin]    Starting Agent: currency_agent[0m
[90m[logging_plugin] 🤖 AGENT STARTING[0m
[90m[logging_plugin]    Agent Name: currency_agent[0m
[90m[logging_plugin]    Invocation ID: e-75bfb9bb-1c95-4140-8b12-72055c3a478b[0m
[90m[logging_plugin] 🧠 LLM REQUEST[0m
[90m[logging_plugin]    Model: gemini-2.5-flash-lite[0m
[90m[logging_plugin]    Agent: currency_agent[0m
[90m[logging_plugin]    System Instruction: 'You are a smart currency conversion assistant.

    For currency conversion requests:
    1. Use `get_fee_for_payment_method()` to find transaction fees
    2. Use `get_exchange_rate()` to get currenc...'[0m
[90m[logging_plugin]    Available Tools: ['get_fee_for_payment_method', 'get_exchange_rate'][0m
[90m[logging_plugin] 🧠 LLM RESPONSE[0m
[90m[logging_plugin]    Agent: currency_agent[0m
[90m[logging_plugin]    Content: function_call: get_fee_for_payment_method | function_call: get_exchange_rate[0m
[90m[logging_plugin]    Token Usage - Input: 593, Output: 49[0m
[90m[logging_plugin] 📢 EVENT YIELDED[0m
[90m[logging_plugin]    Event ID: f6a571e4-efd7-4f05-93d2-12786a5df40c[0m
[90m[logging_plugin]    Author: currency_agent[0m
[90m[logging_plugin]    Content: function_call: get_fee_for_payment_method | function_call: get_exchange_rate[0m
[90m[logging_plugin]    Final Response: False[0m
[90m[logging_plugin]    Function Calls: ['get_fee_for_payment_method', 'get_exchange_rate'][0m
[90m[logging_plugin] 🔧 TOOL STARTING[0m
[90m[logging_plugin]    Tool Name: get_fee_for_payment_method[0m
[90m[logging_plugin]    Agent: currency_agent[0m
[90m[logging_plugin]    Function Call ID: adk-01f5b0a6-ee19-4b8b-800e-696a7d46533b[0m
[90m[logging_plugin]    Arguments: {'method': 'platinum credit card'}[0m
[90m[logging_plugin] 🔧 TOOL COMPLETED[0m
[90m[logging_plugin]    Tool Name: get_fee_for_payment_method[0m
[90m[logging_plugin]    Agent: currency_agent[0m
[90m[logging_plugin]    Function Call ID: adk-01f5b0a6-ee19-4b8b-800e-696a7d46533b[0m
[90m[logging_plugin]    Result: {'status': 'success', 'fee_percentage': 0.02}[0m
[90m[logging_plugin] 🔧 TOOL STARTING[0m
[90m[logging_plugin]    Tool Name: get_exchange_rate[0m
[90m[logging_plugin]    Agent: currency_agent[0m
[90m[logging_plugin]    Function Call ID: adk-692bc033-75ee-47d3-ac6b-5e7219894060[0m
[90m[logging_plugin]    Arguments: {'base_currency': 'USD', 'target_currency': 'EUR'}[0m
[90m[logging_plugin] 🔧 TOOL COMPLETED[0m
[90m[logging_plugin]    Tool Name: get_exchange_rate[0m
[90m[logging_plugin]    Agent: currency_agent[0m
[90m[logging_plugin]    Function Call ID: adk-692bc033-75ee-47d3-ac6b-5e7219894060[0m
[90m[logging_plugin]    Result: {'status': 'success', 'rate': 0.93}[0m
[90m[logging_plugin] 📢 EVENT YIELDED[0m
[90m[logging_plugin]    Event ID: ae5be71e-e8ed-43b8-a9fa-6fbb12bad4d7[0m
[90m[logging_plugin]    Author: currency_agent[0m
[90m[logging_plugin]    Content: function_response: get_fee_for_payment_method | function_response: get_exchange_rate[0m
[90m[logging_plugin]    Final Response: False[0m
[90m[logging_plugin]    Function Responses: ['get_fee_for_payment_method', 'get_exchange_rate'][0m
[90m[logging_plugin] 🧠 LLM REQUEST[0m
[90m[logging_plugin]    Model: gemini-2.5-flash-lite[0m
[90m[logging_plugin]    Agent: currency_agent[0m
[90m[logging_plugin]    System Instruction: 'You are a smart currency conversion assistant.

    For currency conversion requests:
    1. Use `get_fee_for_payment_method()` to find transaction fees
    2. Use `get_exchange_rate()` to get currenc...'[0m
[90m[logging_plugin]    Available Tools: ['get_fee_for_payment_method', 'get_exchange_rate'][0m
[90m[logging_plugin] 🧠 LLM RESPONSE[0m
[90m[logging_plugin]    Agent: currency_agent[0m
[90m[logging_plugin]    Content: text: 'You will receive 450.80 Euros.

Here's how that's calculated:
1. A fee of 2% is charged for using a Platinum Credit Card, which is 10.00 USD.
2. This leaves you with 490.00 USD to convert.
3. The exch...'[0m
[90m[logging_plugin]    Token Usage - Input: 698, Output: 104[0m
[90m[logging_plugin] 📢 EVENT YIELDED[0m
[90m[logging_plugin]    Event ID: 4d3f8929-3958-4471-be3a-4c9ba856f24a[0m
[90m[logging_plugin]    Author: currency_agent[0m
[90m[logging_plugin]    Content: text: 'You will receive 450.80 Euros.

Here's how that's calculated:
1. A fee of 2% is charged for using a Platinum Credit Card, which is 10.00 USD.
2. This leaves you with 490.00 USD to convert.
3. The exch...'[0m
[90m[logging_plugin]    Final Response: True[0m
currency_agent > You will receive 450.80 Euros.

Here's how that's calculated:
1. A fee of 2% is charged for using a Platinum Credit Card, which is 10.00 USD.
2. This leaves you with 490.00 USD to convert.
3. The exchange rate from USD to EUR is 0.93, so 490.00 USD is 455.70 EUR.
[90m[logging_plugin] 🤖 AGENT COMPLETED[0m
[90m[logging_plugin]    Agent Name: currency_agent[0m
[90m[logging_plugin]    Invocation ID: e-75bfb9bb-1c95-4140-8b12-72055c3a478b[0m
[90m[logging_plugin] ✅ INVOCATION COMPLETED[0m
[90m[logging_plugin]    Invocation ID: e-75bfb9bb-1c95-4140-8b12-72055c3a478b[0m
[90m[logging_plugin]    Final Agent: currency_agent[0m
