from flask import Flask, render_template, request,render_template_string

app = Flask(__name__)

def calculate_profit(product_price, cost_price, selling_price, num_orders, return_rate, cpc):
    # Calculate total revenue
    total_revenue = selling_price * num_orders * (1 - return_rate)

    # Calculate total expenses
    total_expenses = (cost_price + cpc) * num_orders

    # Calculate profit
    profit = total_revenue - total_expenses

    return profit

def calculate_profit_status(profit):
    if profit >= 0:
        return "Profit"
    else:
        return "Loss"
    
def calculate_current_roas(actual_revenue, actual_advertising_spend):
    return actual_revenue / actual_advertising_spend if actual_advertising_spend != 0 else 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product_cost_price = float(request.form['cost_price'])
        product_selling_price = float(request.form['selling_price'])
        num_orders = int(request.form['num_orders'])
        return_to_order_ratio = float(request.form['return_rate'])
        cost_per_click = float(request.form['cpp'])

        # Calculate the required ROAS to break even
        total_revenue = product_selling_price * num_orders * (1 - return_to_order_ratio)
        total_expenses = (product_cost_price + cost_per_click) * num_orders
        required_roas = total_revenue / total_expenses if total_expenses != 0 else 0
        
        # Calculate the current ROAS based on actual data
        actual_revenue = num_orders * product_selling_price           
        actual_advertising_spend = num_orders * cost_per_click        
        current_roas = calculate_current_roas(actual_revenue, actual_advertising_spend)

        
        # Calculate the profit
        net_profit = calculate_profit(product_selling_price, product_cost_price, product_selling_price, num_orders, return_to_order_ratio, cost_per_click,)

        profit_status = calculate_profit_status(net_profit)

        return render_template('result.html', profit=net_profit, roas=required_roas, profit_status=profit_status, num_orders=num_orders,current_roas=current_roas)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
