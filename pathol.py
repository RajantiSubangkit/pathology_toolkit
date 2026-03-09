import streamlit as st

st.title("Bogor Vet. Pathol. Lab Toolkit")

st.sidebar.title("Calculator Menu")

menu = st.sidebar.selectbox(
    "Choose Tool",
    [
        "10% Neutral Buffered Formalin",
        "Alcohol Dilution",
        "Antibody Dilution (IHC)",
        "PBS Preparation"
    ]
)

# ===============================
# 10% Neutral Buffered Formalin
# ===============================

if menu == "10% Neutral Buffered Formalin":

    st.header("10% Neutral Buffered Formalin Calculator")

    volume = st.number_input(
        "Final volume (Liters)",
        min_value=0.1,
        key="nbf_volume"
    )

    if st.button("Calculate NBF"):

        formaldehyde = 100 * volume
        NaH2PO4 = 4 * volume
        Na2HPO4 = 6.5 * volume
        water = (1000 * volume) - formaldehyde

        st.subheader("Required Components")

        st.write("37–40% Formaldehyde:", round(formaldehyde,2), "mL")
        st.write("NaH2PO4:", round(NaH2PO4,2), "g")
        st.write("Na2HPO4:", round(Na2HPO4,2), "g")
        st.write("Distilled Water:", round(water,2), "mL")

# ===============================
# Alcohol Dilution
# ===============================

elif menu == "Alcohol Dilution":

    st.header("Alcohol Dilution Calculator")

    C1 = st.number_input("Stock concentration (%)", key="alc_c1")
    C2 = st.number_input("Final concentration (%)", key="alc_c2")
    V2 = st.number_input("Final volume (mL)", key="alc_v2")

    if st.button("Calculate Alcohol"):

        V1 = (C2 * V2) / C1
        water = V2 - V1

        st.subheader("Results")

        st.write("Stock alcohol:", round(V1,2), "mL")
        st.write("Distilled water:", round(water,2), "mL")

# ===============================
# Antibody Dilution
# ===============================

elif menu == "Antibody Dilution (IHC)":

    st.header("IHC Antibody Dilution Calculator")

    dilution = st.text_input(
        "Dilution ratio (example 1:200)",
        key="ab_ratio"
    )

    volume = st.number_input(
        "Final volume (µL)",
        key="ab_volume"
    )

    if st.button("Calculate Antibody"):

        try:

            ratio = int(dilution.split(":")[1])

            antibody = volume / ratio
            diluent = volume - antibody

            st.subheader("Results")

            st.write("Primary antibody:", round(antibody,2), "µL")
            st.write("Diluent:", round(diluent,2), "µL")

        except:

            st.error("Format must be like 1:200")

# ===============================
# PBS Calculator
# ===============================

elif menu == "PBS Preparation":

    st.header("PBS Preparation Calculator")

    volume = st.number_input(
        "Volume (Liters)",
        key="pbs_volume"
    )

    if st.button("Calculate PBS"):

        NaCl = 8 * volume
        KCl = 0.2 * volume
        Na2HPO4 = 1.44 * volume
        KH2PO4 = 0.24 * volume

        st.subheader("Required Components")

        st.write("NaCl:", round(NaCl,2), "g")
        st.write("KCl:", round(KCl,2), "g")
        st.write("Na2HPO4:", round(Na2HPO4,2), "g")
        st.write("KH2PO4:", round(KH2PO4,2), "g")
