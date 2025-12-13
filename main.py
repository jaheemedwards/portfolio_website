import streamlit as st
from projects import projects

def show_projects(projects, filter_tags=None):
    """
    Display projects in a clean layout with images, tech stack, and tags.
    
    :param projects: List of project dictionaries.
    :param filter_tags: Optional list of tags to filter projects.
    """
    for p in projects:
        # Skip project if it doesn't match filter tags
        if filter_tags and not any(tag in p.get("tags", []) for tag in filter_tags):
            continue

        # Container for each project
        with st.container():
            cols = st.columns([1, 2])  # Image left, details right
            
            with cols[0]:
                if "image" in p:
                    st.image(p["image"], width='content')

            with cols[1]:
                st.subheader(p["title"])
                st.write(p.get("desc", ""))

                # Role and date
                role_date = ""
                if "role" in p:
                    role_date += f"**Role:** {p['role']}  "
                if "date" in p:
                    role_date += f"**Date:** {p['date']}"
                if role_date:
                    st.write(role_date)

                # Tech stack badges
                if "tech_stack" in p:
                    st.write("**Tech Stack:**")
                    st.markdown(" ".join([f"`{tech}`" for tech in p["tech_stack"]]))

                # Tags
                if "tags" in p:
                    st.write("**Tags:**")
                    st.markdown(", ".join([f"`{tag}`" for tag in p["tags"]]))

                # Links
                links = []
                if "link" in p and p["link"]:
                    links.append(f'<a href="{p["link"]}" style="color: #1a0dab; text-decoration: underline;" target="_blank">🔗 Live Demo</a>')
                if "github_link" in p and p["github_link"]:
                    links.append(f'<a href="{p["github_link"]}" style="color: #1a0dab; text-decoration: underline;" target="_blank">💻 GitHub</a>')

                if links:
                    st.markdown(" | ".join(links), unsafe_allow_html=True)


            st.divider()


email = "jaheemedwardswork@gmail.com"
resume_path = "assets/Resume with CL Jaheem Edwards.pdf"

st.set_page_config(page_title="Portfolio", layout="wide")

tabs = st.tabs(["About", "Projects"])

with tabs[0]:
    # Split page into two columns: text on the left, image on the right
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("Hello, I'm Jaheem Edwards")
        paragraph_text = '''
            Jaheem Edwards possesses a BSc in Computer Science from the UWI. He is a Data Scientist in leading companies implementing AI systems. He completed various certificates in Data Science, Machine and Deep Learning assisting in projects namely, News Analytics Dashboard, Automated Data Warehouse and Customer Churn Prediction. 

            He brings expertise in collaborating with cross-functional teams to discover pain points and solve problems with data science principles or technical solutions. Communication, strategic thinking, conceptualization and guiding stakeholder decisions through data are skills he applies, providing a diverse and holistic approach. 

            Beyond his career, he is an anime fan who passionately practices jiu-jitsu and chess. He is fond of researching innovative technologies as he is deeply curious about AI transformations in industries, motivated by this, he brings an analytical perspective and visionary mindset to challenges. 

            Jaheem’s goal is to push boundaries of data science, drive innovation and thrive as a technology leader.
        '''

        st.write(paragraph_text)
        
        # Action buttons
        btn_col1, btn_col2, btn_col3, btn_col4 = st.columns(4)
        with btn_col1:
            st.download_button(
                "📄 Download Resume",
                open(resume_path, "rb").read(),
                "Jaheem_Edwards_Resume.pdf"
            )
        with btn_col2:
            st.markdown(
                """<a href='https://github.com/jaheemedwards' target='_blank'>
                    <button style='padding:8px 16px; font-size:16px;'>💻 GitHub</button>
                </a>""",
                unsafe_allow_html=True
            )

        with btn_col3:
            st.markdown(
                """<a href='https://www.linkedin.com/in/jaheem-edwards/' target='_blank'>
                    <button style='padding:8px 16px; font-size:16px;'>🔗 LinkedIn</button>
                </a>""",
                unsafe_allow_html=True
            )


        with btn_col4:
            st.markdown(f"""
    <button onclick="navigator.clipboard.writeText('{email}')"
            style="padding:8px 16px; font-size:16px;">
        {email}
    </button>
""", unsafe_allow_html=True)


    with col2:
        st.image("assets/portfolio_photo.jpg", caption="Jaheem Edwards", width='stretch')

with tabs[1]:
    st.header("Projects")
    show_projects(projects)
