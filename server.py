import os
from fastmcp import FastMCP
import requests

mcp = FastMCP("Life-Ops-Agent")

# Goal: Proactive Vacation Planning logic
@mcp.tool()
def get_vacation_strategy(days_until_weekend: int):
    """
    Analyzes Seattle weather forecast to trigger Plan A or Plan B.
    """
    # Simple Seattle Weather Check (Example API)
    # In a real scenario, use a weather API key here
    forecast = "Sunny/Dry" # Placeholder: Logic would fetch actual SEA forecast
    
    if "Sunny" in forecast and days_until_weekend > 30:
        return {
            "strategy": "Plan A (Local)",
            "action": "Search dog-friendly cabins within 150 miles of 98117.",
            "status": "Discovery Phase (T-45)"
        }
    else:
        return {
            "strategy": "Plan B (Escape)",
            "action": "Search Alaska/Delta flights from SEA to SUNNY hubs.",
            "status": "Pivot Active"
        }

# Goal: Home Maintenance Trigger
@mcp.tool()
def check_home_maintenance(current_month: int):
    """Triggers maintenance tasks for 7341 27th Ave NW based on Seattle seasons."""
    if current_month in [10, 11]:
        return "Action: Schedule Gutter Cleaning for 7341 27th Ave NW."
    if current_month in [6, 7, 8]:
        return "Action: Adjust Irrigation for dry Seattle summer."
    return "Status: Home systems nominal."

if __name__ == "__main__":
    mcp.run()
