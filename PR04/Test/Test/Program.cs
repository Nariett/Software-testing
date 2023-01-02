using System;
using System.Security.Policy;

namespace Test
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double[,] matrix = new double[4, 4]
            {
                {2,6,1,8 },
                {8,2,5,2 },
                {9,3,2,5 },
                {2,3,7,2 },
            };
            Matrix x = new Matrix();
            x.SetUp();
            x.Print();
            Console.WriteLine();
            x.Print();
            Console.WriteLine(x.Square(matrix));
            Console.ReadKey();
        }
    }
    public class Matrix
    {
        private double[,] matrix;
        public void SetUp()
        {
            matrix = new double[4, 4]
            {
                {2,6,1,8 },
                {8,2,5,2 },
                {9,3,2,5 },
                {2,3,7,2 },
            };
        }
        public void Print()
        {
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    Console.Write($"{matrix[i, j]} ");
                }
                Console.WriteLine("");
            }
        }
        public double Max(double[,] matrix)//работает 
        {
            double max = 0;
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    if (max < matrix[i, j])
                    {
                        max = matrix[i, j];
                    }
                }
            }
            return max;
        }
        public void Select(double[,] matrix )//смена 
        {
            for (int i = 0; i < matrix.GetLength(0); i++)
            {
                if (i % 2 == 0)
                {
                    matrix[i, i] = Max(matrix);
                }
                else matrix[i, i] = Math.Pow(matrix[i, i], 2);
            }

        }
        public double SecondDiagonal(double[,] matrix)//работает сумма побочной
        {
            double sum = 0;
            for (int i = 0; i < matrix.GetLength(0); i++)
            {
                sum += matrix[i, matrix.GetLength(0) - i - 1];
            }
            return sum;
        }
        public bool Square(double[,] matrix)
        {
            if(matrix.GetLength(0) == matrix.GetLength(1))
            {
                return true;
            }
            return false;
        }
    }
}
