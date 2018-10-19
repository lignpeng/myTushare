var mockData ={"D": [["1", "2", "3"], ["4", "5", "6"]]}

window.getMockData = function (fullCode, type) {
    if (mockData[type]) {
        return mockData[type]
    }
    return []
}
    