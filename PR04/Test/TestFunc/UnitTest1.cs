using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Diagnostics.Contracts;
using System.Diagnostics.Metrics;
using System.Drawing;
using System.Reflection.Emit;
using Test;

namespace TestFunc
{
    [TestClass]
    public class MatrixTest
    {
        double [,] matrix;
        [TestInitialize]
        public void SetUp()
        {
            matrix = new double[4, 4]
            {
                {3,6,1,8 },
                {8,0,5,2 },
                {9,3,6,5 },
                {2,3,7,1 },
            };
        }
        [TestMethod]
        public void MaxReturm()//работает макс значение
        {
            Matrix test = new Matrix();
            double expected = 9;
            double max = test.Max(matrix);
            Assert.AreEqual(expected, max);
        }
        [TestMethod]
        public void SecondDiagonal()//работает сумма побочной
        {
            Matrix test = new Matrix();
            double expected = 18;
            double sum = test.SecondDiagonal(matrix);
            Assert.AreEqual(expected,sum);
        }
        [TestMethod]
        public void Select()//замена 
        {
            Matrix test = new Matrix();
            test.Select(matrix);
            double expected = 9;
            double rez = matrix[0, 0];
            Assert.AreEqual(expected, rez);
        }
        [TestMethod]
        public void Square()
        {
            Matrix test = new Matrix();
            bool expected = true;
            bool rez = test.Square(matrix);
            Assert.AreEqual(expected, rez);
        }
    }
}