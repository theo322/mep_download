import streamlit as st
import pandas as pd

df = pd.read_excel("data.xlsx",sheet_name="Export")

pd.options.display.float_format = '{:,.2f}'.format

st.set_page_config(page_title= "Download M&P", page_icon="🗂️")

#INTRO
st.title("Melhores e Piores")
st.write(":red[Data de atualização:10/06/2024]")
st.header("Aqui você pode baixar a base do melhores e piores!")
st.subheader("Escolha uma família")


options = ["01 Lar", "02 Masculino", '03 Feminino', "04 Infantil", "05 Calçados", "10 Acessorios Av"]
familia = st.radio("",
                    options= options, 
                    index=None, 
                    on_change=None)

if familia is not None:
    # Filter the DataFrame based on the selected family
    df_fam = df[df["Familia - Family"] == familia]
    
    # Manually format DataFrame columns
    formatted_df = df_fam.copy()
    for col in formatted_df.select_dtypes(include=['float64']).columns:
        formatted_df[col] = formatted_df[col].apply(lambda x: int(x) if x.is_integer() else '{:,.4f}'.format(x).replace('.',','))

    # Convert "Item" column to string and remove commas
    formatted_df["Item"] = formatted_df["Item"].astype(str).str.replace(",", "")
    formatted_df["VND TT 12s"] = formatted_df["VND TT 12s"].astype(str).str.replace(",", "")
    formatted_df["Estoque QTD Inicial Initial Stock Qty"] = formatted_df["Estoque QTD Inicial Initial Stock Qty"].astype(str).str.replace(",", "")
    formatted_df["Recebimento Total  Total Recieved"] = formatted_df["Recebimento Total  Total Recieved"].astype(str).str.replace(",", "")
    formatted_df["Idade de Estoque - Days in Stock"] = formatted_df["Idade de Estoque - Days in Stock"].astype(str).str.replace(",", "")
    formatted_df["Idade Ajustada - Days in Stock (adjusted)"] = formatted_df["Idade Ajustada - Days in Stock (adjusted)"].astype(str).str.replace(",", "")
    formatted_df["Cash Margem Mês - Monthly Cash Margin"] = formatted_df["Cash Margem Mês - Monthly Cash Margin"].astype(str).str.replace(",", "")
    formatted_df["Venda R$ Mês - Montly Sales in R$"] = formatted_df["Venda R$ Mês - Montly Sales in R$"].astype(str).str.replace(",", "")
    formatted_df["R$ Estoque - Stock in R$"] = formatted_df["R$ Estoque - Stock in R$"].astype(str).str.replace(",", "")
    formatted_df["Estoque QTD - Stock Qty"] = formatted_df["Estoque QTD - Stock Qty"].astype(str).str.replace(",", "")
    formatted_df["Venda QTD Total - Total Sales Qty"] = formatted_df["Venda QTD Total - Total Sales Qty"].astype(str).str.replace(",", "")
    formatted_df["Cash Margem Total - Total Cash Margin"] = formatted_df["Cash Margem Total - Total Cash Margin"].astype(str).str.replace(",", "")
    formatted_df["Carteira Valor - Order Value"] = formatted_df["Carteira Valor - Order Value"].astype(str).str.replace(",", "")
    formatted_df["Carteira QTD - Order Qty"] = formatted_df["Carteira QTD - Order Qty"].astype(str).str.replace(",", "")
    formatted_df["ANO_MÊS - Year_month"] = formatted_df["ANO_MÊS - Year_month"].astype(str).str.replace(",", "")
    formatted_df["Recebimento Custo - Shipping Cost"] = formatted_df["Recebimento Custo - Shipping Cost"].astype(str).str.replace(",", "")
    formatted_df["Recebimento R$ - Amout (R$) Recieved "] = formatted_df["Recebimento R$ - Amout (R$) Recieved "].astype(str).str.replace(",", "")
    formatted_df["Venda QTD Total - Total Sales Qty"] = formatted_df["Venda QTD Total - Total Sales Qty"].astype(str).str.replace(",", "")

    #Display the formatted DataFrame
    st.write(formatted_df)

    
    #st.download_button("Baixar base", data= csv, file_name=f"{familia}_melhores_e_piores.csv", mime="texr/csv")
