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
currency_agent > In order to convert 500 USD to EUR, you will receive 455.7 EUR.

Here's how this amount was calculated:
1. A fee of 2% was charged on the initial amount. The fee was 10 USD (500 * 0.02).
2. The remaining amount was 490 USD (500 - 10).
3. The exchange rate from USD to EUR is 0.93, so the final amount is 455.7 EUR (490 * 0.93).
