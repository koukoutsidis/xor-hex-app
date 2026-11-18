import streamlit as st

st.set_page_config(page_title="XOR & Hex Κρυπτογραφητής", page_icon="🔐", layout="centered")

st.title("🔐 Διαδραστική Κρυπτογράφηση XOR & Hex")
st.markdown("Υποστηρίζει κανονικά ελληνικούς και αγγλικούς χαρακτήρες!")

# --- ΕΝΟΤΗΤΑ 1: ΕΙΣΑΓΩΓΗ ---
st.subheader("1. Μήνυμα και Κλειδί")
message = st.text_input("Αρχικό Μήνυμα:", value="Λύκειο 2026")
key = st.number_input("Κλειδί (αριθμός από 0 έως 255):", min_value=0, max_value=255, value=42)

# --- ΕΝΟΤΗΤΑ 2: ΚΡΥΠΤΟΓΡΑΦΗΣΗ ---
if st.button("🚀 Κρυπτογράφηση σε Hex", type="primary"):
    if message:
        # Μετατροπή κειμένου σε UTF-8 bytes και εφαρμογή XOR byte-by-byte
        message_bytes = message.encode('utf-8')
        encrypted_hex = "".join([f"{b ^ int(key):02X}" for b in message_bytes])
        st.session_state['encrypted_hex'] = encrypted_hex
        st.success("Η κρυπτογράφηση ολοκληρώθηκε επιτυχώς!")
    else:
        st.warning("Παρακαλώ εισάγετε ένα μήνυμα.")

# Αν υπάρχει κρυπτογραφημένο αποτέλεσμα, το εμφανίζουμε
if 'encrypted_hex' in st.session_state:
    st.text_input("Κρυπτογραφημένο αποτέλεσμα (Hex):", value=st.session_state['encrypted_hex'])

st.markdown("---")

# --- ΕΝΟΤΗΤΑ 3: ΑΠΟΚΡΥΠΤΟΓΡΑΦΗΣΗ ---
st.subheader("2. Αποκρυπτογράφηση")
hex_input = st.text_input("Εισάγετε Hex string για αποκρυπτογράφηση:", value=st.session_state.get('encrypted_hex', ''))
decrypt_key = st.number_input("Κλειδί αποκρυπτογράφησης:", min_value=0, max_value=255, value=int(key))

if st.button("⬅️ Αποκρυπτογράφηση"):
    try:
        decrypted_bytes = bytearray()
        # Διαβάζουμε το Hex ανά 2 χαρακτήρες και κάνουμε XOR
        for i in range(0, len(hex_input), 2):
            hex_pair = hex_input[i:i+2]
            byte_val = int(hex_pair, 16)
            decrypted_bytes.append(byte_val ^ int(decrypt_key))
            
        # Μετατροπή των bytes ξανά σε UTF-8 string
        decrypted_message = decrypted_bytes.decode('utf-8')
        st.success(f"**Τελικό Αποκαλυπτόμενο Μήνυμα:** `{decrypted_message}`")
    except Exception as e:
        st.error(f"Σφάλμα αποκρυπτογράφησης! Βεβαιωθείτε ότι το κλειδί και το Hex είναι σωστά.")