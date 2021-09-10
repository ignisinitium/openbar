Persons.QuestionFilter = ChildrenInQuestion
For Each Person in Persons
  Person.Details.Ask()
  Person.NumberOfTrips.Ask()
  Person.Trips.QuestionsFilter = Person.NumberOfTrips
  Person.Trips.Ask()
Next