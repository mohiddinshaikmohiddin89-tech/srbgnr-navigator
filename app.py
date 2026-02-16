import streamlit as st
import webbrowser

# --- CONFIGURATION & STYLING ---
st.set_page_config(
    page_title="SR & BGNR Campus Navigator",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS to make it look like a mobile app
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #004e92;
        color: white;
        height: 50px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #002d55;
    }
    h1 {
        color: #004e92;
        text-align: center;
        font-size: 24px;
    }
    .info-box {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- DATA: COLLEGE LOCATIONS ---
# Coordinates are approximate based on the college location in Khammam
COLLEGE_LAT = 17.2543
COLLEGE_LON = 80.1605

locations = {
    "Principal's Office": {
        "desc": "Located in the Main Administrative Block (Ground Floor).",
        "category": "Admin",
        "lat": 17.2545, "lon": 80.1607
    },
    "Library (Central)": {
        "desc": "Located near the NTR Circle entrance. Offers a vast collection of books and journals.",
        "category": "Academic",
        "lat": 17.2542, "lon": 80.1604
    },
    "Auditorium": {
        "desc": "Main venue for events and seminars. Located opposite the main garden.",
        "category": "Facilities",
        "lat": 17.2540, "lon": 80.1606
    },
    "Computer Labs (JKC & TASK)": {
        "desc": "JKC Lab and TASK Room. Located in the Commerce/Computer Science Block.",
        "category": "Labs",
        "lat": 17.2546, "lon": 80.1608
    },
    "Chemical Lab": {
        "desc": "Located in the Science Wing (Chemistry Dept). Ground Floor.",
        "category": "Labs",
        "lat": 17.2544, "lon": 80.1603
    },
    "Botany/Zoology Labs": {
        "desc": "Science Wing. First Floor.",
        "category": "Labs",
        "lat": 17.2544, "lon": 80.1603
    },
    "Departmental Store": {
        "desc": "Co-operative store for stationery and snacks. Near the entrance.",
        "category": "Facilities",
        "lat": 17.2541, "lon": 80.1602
    },
    "Women Empowerment Cell": {
        "desc": "Located in the Arts Block. A safe space for guidance and support.",
        "category": "Admin",
        "lat": 17.2545, "lon": 80.1609
    },
    "Conference Room": {
        "desc": "Adjacent to the Principal's Chamber. Used for staff meetings.",
        "category": "Admin",
        "lat": 17.2545, "lon": 80.1607
    },
    "Play Ground": {
        "desc": "Large ground behind the main building (connected to Sardar Patel Stadium).",
        "category": "Facilities",
        "lat": 17.2535, "lon": 80.1600
    },
    "Departments (Arts/Commerce/Science)": {
        "desc": "Classrooms are spread across the U-shaped Main Building.",
        "category": "Academic",
        "lat": 17.2543, "lon": 80.1605
    }
}

# --- APP LAYOUT ---

# Header with Logo Placeholder (Text-based for code simplicity)
st.markdown("<h1>🎓 SR & BGNR Smart Navigator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Khammam • NAAC A++ • Autonomous</p>", unsafe_allow_html=True)

# Navigation Menu
menu = st.radio("Go to:", ["🏠 Home", "🗺️ Find a Location", "ℹ️ About College"], horizontal=True)

if menu == "🏠 Home":
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/SR_BGNR_Govt_Degree_College_Khammam.jpg/800px-SR_BGNR_Govt_Degree_College_Khammam.jpg", 
             caption="SR & BGNR Govt Arts & Science College", use_container_width=True)
    
    st.markdown("""
    <div class='info-box'>
        <h3>Welcome Students & Visitors!</h3>
        <p>Use this app to navigate the SR & BGNR campus. Locate labs, the library, and administrative offices easily.</p>
    </div>
    """, unsafe_allow_html=True)

    # Quick Action Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📍 Library"):
            st.session_state['search'] = "Library (Central)"
            st.rerun() # Refresh to jump to navigator
    with col2:
        if st.button("🏆 Sports"):
            st.session_state['search'] = "Play Ground"
            st.rerun()

elif menu == "🗺️ Find a Location":
    st.subheader("Where do you want to go?")
    
    # Category Filter
    category = st.selectbox("Filter by Category", ["All", "Admin", "Academic", "Labs", "Facilities"])
    
    # Filter list based on selection
    filtered_locs = {k: v for k, v in locations.items() if category == "All" or v['category'] == category}
    
    # Dropdown to select location
    selection = st.selectbox("Select Destination", list(filtered_locs.keys()))
    
    if selection:
        loc_data = locations[selection]
        
        st.markdown(f"""
        <div class='info-box'>
            <h3>📍 {selection}</h3>
            <p><b>Details:</b> {loc_data['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Google Maps Direct Link
        # Generates a link that opens the Google Maps app with directions to the specific coordinates
        gmaps_url = f"https://www.google.com/maps/dir/?api=1&destination={loc_data['lat']},{loc_data['lon']}"
        
        st.link_button(f"🚀 Navigate to {selection}", gmaps_url)
        
        # Simple Map Visualization
        st.map(data={'lat': [loc_data['lat']], 'lon': [loc_data['lon']]}, zoom=18)

elif menu == "ℹ️ About College":
    st.markdown("""
    <div class='info-box'>
        <h3>SR & BGNR Govt Arts & Science College</h3>
        <ul>
            <li><b>Status:</b> Autonomous, NAAC A++ (3.64 CGPA)</li>
            <li><b>Established:</b> 1956</li>
            <li><b>Location:</b> Yellandu Road, Khammam, Telangana</li>
            <li><b>Affiliation:</b> Kakatiya University</li>
        </ul>
        <p>This college is one of the premier institutions in the state, offering various UG and PG courses.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("App developed for easy campus navigation.")
