from application import Subject, Observer

subject = Subject()

UiObserver = Observer()
LogObserver = Observer()
AlertsObserver = Observer()

subject.registerObserver(UiObserver)
subject.registerObserver(LogObserver)
subject.registerObserver(AlertsObserver)


subject.update_data("AlertsObserver")