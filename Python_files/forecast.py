import streamlit as st
from PIL import Image

def show_forecast_page():

    st.set_page_config(
        page_title="Inventory Management",
        page_icon=":chart:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Load images
    image1 = Image.open("D:/EL/Inventory_management/graphs/t20.png")
    image2 = Image.open("D:/EL/Inventory_management/graphs/t50.png")
    image3 = Image.open("D:/EL/Inventory_management/graphs/spare parts.png")
    image4 = Image.open("D:/EL/Inventory_management/graphs/weekly_demand.png")
    image5 = Image.open("D:/EL/Inventory_management/graphs/weekly_demand 2.png")


    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st.markdown("<h2 style='text-align: center; color: white; background-color: #007bff'>TOP 20 Best Selling Parts</h2>", unsafe_allow_html=True)
        button1 = st.button("Click to view", key='btn1')
    with col2:
        st.markdown("<h2 style='text-align: center; color: white; background-color: #ff69b4'>TOP 50 Best Selling Parts</h2>", unsafe_allow_html=True)
        button2 = st.button("Click to view", key='btn2')
    with col3:
        st.markdown("<h2 style='text-align: center; color: white; background-color: #33cc33'>Sales Forecasting</h2>", unsafe_allow_html=True)
        button3 = st.button("Click to view", key='btn3')
    with col4:
        st.markdown("<h2 style='text-align: center; color: white; background-color: #ff9900'>Weekly demands</h2>", unsafe_allow_html=True)
        button4 = st.button("Click to view", key='btn4')

    if button1:
        st.title("TOP 20 Best Selling Parts")
        st.image(image1, use_column_width=True)
        st.text("Filter-Oil: With nearly 3500 occurrences, this spare part dominates the list. It likely represents"
                "\n frequent oil filter replacements, essential for engine health.Air Filter, Brake Pad, and Oil: These "
                "\nfollow, showing moderate demand. Air filters and brake pads are crucial for safety and performance,"
                "\n while oil is a recurring need.Suspension, Battery, and Headlight: These appear further down, suggesting "
                "\nless frequent replacements. Suspension components and batteries endure longer, while headlights may need "
                "\noccasional attention.Predictions for the Future: Based on the trend, we can anticipate continued high"
                "\n demand for “Filter-Oil.” However, as electric vehicles gain prominence, traditional components like "
                "\noil filters might decline. Keep an eye on emerging technologies and adjust inventory accordingly.")
    elif button2:
        st.title("TOP 50 Best Selling Parts")
        st.image(image2, use_column_width=True)
        st.text("This bar graph provides a detailed breakdown of demand for the top 50 spare parts, displaying a classic"
                "\nlong-tail distribution where a small number of parts account for a disproportionately large share of total"
                "\ndemand. The top item, labeled DOUBLE_END, shows a demand of nearly 3,800 units, significantly higher"
                "\nthan any other part. The second most popular item, possibly \"STEERING,\" has a demand of about 1,800 units,"
                "\nless than half of the top item. This sharp drop-off continues down the list, with the 10th most popular item "
                "\nhaving a demand of only about 500 units.Given this distribution, it is preferable that a tiered approach "
                "\nto inventory management be adopted. For the top 5-10 items, which represent the bulk of demand, it is"
                "\npreferable that high stock levels be maintained. These items should rarely, if ever, be out of stock."
                "\nImplementing an automatic reordering system for these high-demand parts would ensure consistent availability."
                "\nFor the middle-range items (roughly items 11-30), it is preferable that a more balanced approach be taken."
                "\nThese items have significant demand but not enough to justify the same high stock levels as the top items."
                "\nJust-in-time inventory practices might be appropriate here, balancing availability against storage costs."
                "\nFor the long tail of low-demand items (roughly items 31-50 and beyond), it is preferable that a minimal"
                "\nstocking approach be considered. These items could be ordered on demand or kept in very low quantities."
                "\nSome might even be candidates for discontinuation if their carrying costs outweigh their profit contribution."
                "\nIt is preferable that the factors driving the popularity of the top items be investigated thoroughly. "
                "\nUnderstanding whether these parts are prone to frequent replacement, are universal parts that fit multiple models,"
                "\nor have other characteristics driving their high demand can help in predicting future demand patterns and potentially "
                "\nidentifying upcoming high-demand items.It is also preferable that this analysis be updated regularly, as demand patterns can shift over time."
                "\nA part that's low-demand now might become crucial in the future due to changes in the market or product lifecycles. Conversely, currently popular parts "
                "\nmight see declining demand. By staying attuned to these shifts, the inventory mix can be continuously optimized to match current market needs")
    elif button3:
        st.title("Sales Forecasting")
        st.image(image3, use_column_width=True)
        st.text("This line graph illustrates the weekly demand for spare parts over an extended period, likely spanning"
                "\nfrom July 2023 to January 2024. The graph reveals a complex pattern of demand characterized by high "
                "\nvolatility, seasonal fluctuations, and an overall upward trend. Weekly demand fluctuates dramatically,"
                "\nranging from lows of around 100 units to peaks exceeding 500 units.Given this high degree of volatility,"
                "\nit is preferable that a highly responsive inventory management system be implemented. This system should "
                "\nbe capable of adjusting to short-term changes while also maintaining enough stock to meet unexpected spikes"
                "\nin demand. Despite the short-term volatility, a general upward trend is discernible over the entire period,"
                "\nsuggesting a gradually expanding market for spare parts.It is preferable that long-term planning take this"
                "\ntrend into account, potentially expanding capacity over time, both in terms of inventory levels and "
                "\nphysical storage space. Seasonal patterns appear to be present in the data, with higher peaks observed in"
                "\nthe latter half of each year. It is preferable that these seasonal patterns be anticipated and factored"
                "\ninto inventory planning.The graph also shows occasional sharp drops in demand, including one instance"
                "\nwhere demand falls to nearly zero. It is preferable that these extreme events be thoroughly investigated,"
                "\nas they might represent data anomalies, supply chain disruptions, or other external factors affecting"
                "\nthe market.Given these observations, it is preferable that a sophisticated and flexible inventory management"
                "\napproach be adopted:It is preferable that a robust forecasting system be implemented, capable of accounting"
                "\nfor both the overall trend and seasonal patterns. This might involve using advanced statistical methods or "
                "\neven machine learning algorithms to predict demand.It is preferable that higher safety stock levels be maintained"
                "\nduring peak seasons to handle demand spikes. The exact level should be balanced against carrying costs and the risk of"
                "\nobsolescence.It is preferable that contingency plans be developed for extreme events, both unexpected spikes"
                "\nand drops in demand. This might involve having flexible supplier agreements or maintaining emergency cash reserves."
                "\nIt is preferable that dynamic pricing strategies be considered. During periods of low demand, targeted promotions or discounts could"
                "\nhelp stimulate sales and smooth out some of the volatility.It is preferable that inventory levels be regularly"
                "\nreviewed and adjusted based on the observed upward trend. This might involve gradually increasing overall stock"
                "\nlevels or expanding storage capacity.It is preferable that the causes of major demand fluctuations be investigated"
                "\nthoroughly. Understanding whether they're tied to specific events, economic conditions, or changes in the customer "
                "\nbase can improve future forecasting accuracy and inform strategic decision-making.By carefully analyzing and responding "
                "\nto the patterns revealed in this graph, inventory management can be optimized, customer satisfaction can be improved "
                "\nthrough consistent parts availability, and the business can be positioned for long-term growth in a dynamic market.")
    elif button4:
        st.title("Weekly demands")
        st.image(image4, use_column_width=True)
        st.image(image5, use_column_width=True)
        st.text("The two graphs, \"Spare Parts Demand per Week\" and \"Weekly Demand Forecast,\" provide complementary"
                "\ninsights into demand patterns over different time scales. Both reveal significant volatility and an"
                "\n overall upward trend in demand, suggesting a complex and dynamic market for spare parts.The \"Spare "
                "\nParts Demand per Week\" graph spans a longer period, likely from July 2023 to January 2024, showing "
                "\ndramatic fluctuations ranging from 100 to over 500 units weekly. It reveals seasonal patterns with higher"
                "\n peaks in the latter half of each year. The \"Weekly Demand Forecast\" focuses on a shorter 7-week period,"
                "\nwith demand varying between 275 and 425 units, exhibiting similar volatility but on a more granular"
                "\nscale.Given these observations, it is preferable that a sophisticated, flexible, and highly responsive"
                "\ninventory management system be implemented. This system should be capable of handling both short-term "
                "\nfluctuations and long-term trends, adjusting rapidly to weekly changes while also accounting for seasonal"
                "\npatterns and the overall upward trend.It is preferable that advanced forecasting methods be employed,"
                "\ncombining short-term techniques like exponential smoothing or ARIMA models for weekly predictions with"
                "\nlonger-term forecasting that incorporates seasonal factors and trend analysis. This dual approach can"
                "\nhelp in making accurate predictions across different time horizons, allowing for timely adjustments to"
                "\ninventory levels.Safety stock levels should be carefully managed. It is preferable that these be increased"
                "\nto buffer against unexpected demand spikes, as seen in both graphs. However, this must be balanced against"
                "\nthe risk of overstocking during low-demand periods. The exact levels should be dynamically adjusted based"
                "\non seasonal expectations and recent demand patterns.Given the overall upward trend observed in both graphs,"
                "\nit is preferable that long-term planning account for gradually expanding capacity, both in terms of inventory "
                "\nlevels and physical storage space. This might involve negotiating more frequent deliveries from suppliers or"
                "\nexploring options for flexible storage solutions.It is preferable that contingency plans be developed "
                "\nfor extreme events, including both unexpected spikes and sharp drops in demand. These plans might include "
                "\nflexible supplier agreements, emergency cash reserves, or strategies for rapid inventory adjustment.Dynamic"
                "\npricing strategies should be considered, especially for managing the seasonal fluctuations observed in the "
                "\nlonger-term graph. During periods of historically low demand, targeted promotions or discounts could help"
                "\nstimulate sales and smooth out some of the volatility.Finally, it is preferable that the causes of major"
                "\ndemand fluctuations be thoroughly investigated. This includes understanding seasonal effects, potential "
                "\nmarket shifts, and any external factors that might be influencing demand patterns. This deep understanding"
                "\ncan inform both short-term inventory decisions and long-term strategic planning.By integrating insights from "
                "\nboth short-term and long-term demand patterns, inventory management can be optimized to improve customer"
                "\nsatisfaction through consistent parts availability while positioning the business for sustainable growth "
                "\nin this dynamic market.")

    st.text("Demand Forecasting Project Report\nIntroduction")
    st.text("In this project, we developed a machine learning model to forecast the demand for spare parts. Accurate demand "
            "\nforecasting is essential for optimizing inventory management and ensuring the availability of stock to meet "
            "\ncustomer needs without incurring the costs associated with overstocking")
    st.text("Methodology\nWe collected and preprocessed historical sales data, which involved handling missing values,"
            " normalizing the data, and creating time-series features. The data was then split into training and test sets "
            "for model evaluation.")
    st.text("Using this data, we trained several machine learning models and selected the best-performing model based on "
            "cross-validation results. This model was then used to make predictions on the test data.")
    st.text("Results\nOur model achieved the following performance metrics:\nMean Absolute Error (MAE): 86.97\nRoot Mean Squared Error (RMSE): 103.46\nAccuracy: 76.73%\nPrecision: 76.73%\nAn accuracy and precision of 76.73% are particularly notable,"
            " indicating the model's strong ability to make accurate predictions. These metrics highlight the effectiveness of our approach\nin forecasting demand, which is critical for efficient inventory management.")
    st.text("Discussion\nIn the context of demand forecasting, an accuracy rate above 70% is generally considered good. "
            "Ourmodel surpasses this benchmark, achieving 76.73%,\n which is a strong indicator of its reliability."
            "\n This level of accuracy is valuable for industries where demand volatility can significantly impact inventory"
            " management.")

    st.text("Conclusion\nThe project successfully developed a demand forecasting model with an accuracy of 76.73%, demonstrating\n"
            " its robustness and potential for practical application in inventory management. The results underscore the model's ability to provide reliable \n"
            "demand forecasts, thereby enhancing decision-making and operational efficiency.")
    st.text("Recommendations\nModel Enhancement: Continue to refine the model to further improve accuracy.\n"
            "Feature Integration: Consider adding external factors, such as economic indicators and market trends, "
            "to enhance predictive power.\nScability: Ensure the model can scale to accommodate larger datasets and more extensive forecasting requirements as the business grows.\n"
            "Our demand forecasting model stands out as a reliable tool for optimizing inventory management and ensuring that customer needs are met efficiently.")

    if st.sidebar.button("Back to Home"):
        st.session_state.page = 'main'

if __name__ == "__main__":
    show_forecast_page()
