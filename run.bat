pip install virtualenv
newenv\Scripts\activate
pytest -s -v -m "sanity" --html=reports/group.html testcases/ --browser chrome
rem pytest -s -v -m "sanity" --html=reports/groupfirefox.html testcases/ --browser firefox

rem pytest -s -v -m "sanity or regression" --html=reports/group.html testcases/ --browser chrome

rem pytest -s -v -m "sanity and regression" --html=reports/group.html testcases/ --browser chrome

rem pytest -s -v -m "regression" --html=reports/group.html testcases/ --browser chrome


