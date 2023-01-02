using Test;

namespace TestUnit
{
    public class Tests
    {
        double[,] matrix;
        [SetUp]
        public void Setup()
        {
            
            matrix = new double[4, 4]
           {
                {3,6,1,8 },
                {8,0,5,2 },
                {9,3,6,5 },
                {2,3,7,1 },
           };
        }

        [Test]
        public void MaxReturm()
        {
            Matrix test = new Matrix();
            double expected = 9;
            double max = test.Max(matrix);
            Assert.AreEqual(expected, max);
        }
        [Test]
        public void SecondDiagonal()//работает сумма побочной
        {
            Matrix test = new Matrix();
            double expected = 18;
            double sum = test.SecondDiagonal(matrix);
            Assert.AreEqual(expected, sum);
        }
        [Test]
        public void Select()//замена 
        {
            Matrix test = new Matrix();
            test.Select(matrix);
            double expected = 9;
            double rez = matrix[0, 0];
            Assert.AreEqual(expected, rez);
        }
        [Test]
        public void Square()
        {
            Matrix test = new Matrix();
            bool expected = true;
            bool rez = test.Square(matrix);
            Assert.AreEqual(expected, rez);
        }
    }
}