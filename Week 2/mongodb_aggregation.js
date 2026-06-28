db.students.insertMany([
    { name: "Alice", department: "CSE", marks: 90 },
    { name: "Bob", department: "ECE", marks: 75 },
    { name: "Charlie", department: "CSE", marks: 85 },
    { name: "David", department: "EEE", marks: 65 }
]);

db.students.aggregate([
    {
        $match: {
            marks: { $gte: 80 }
        }
    },
    {
        $project: {
            _id: 0,
            name: 1,
            department: 1,
            marks: 1
        }
    }
]);
