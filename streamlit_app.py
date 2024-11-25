import streamlit as st

from llm_parser import parse_by_ollama
from scraper_using_own_driver import scrape_url
from scraper_using_own_driver import extract_body_content, clean_content, split_dom_into_sections

st.title("Scrapping using LLM")
url = st.text_input("Enter the URL of the website to scrape")


if st.button("Scrape"):
    st.write("Scraping the website...")
    st.write(url)

    # get the page source
    page_source = scrape_url(url)
    # st.write(page_source)
    body_content = extract_body_content(page_source)
    cleaned_content = clean_content(body_content)
    sections = split_dom_into_sections(cleaned_content)

    st.session_state.dom_content = cleaned_content
    
    with st.expander("Body Content"):
        st.text_area("Body Content", value=cleaned_content, height=400)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse"):
        if parse_description:
            st.write("Parsing the dom content...")
            dum_chunks = split_dom_into_sections(st.session_state.dom_content)
            st.write("Chunking done")
            results = parse_by_ollama(dom_chunks=dum_chunks,parse_description=parse_description)
            st.write(results)
