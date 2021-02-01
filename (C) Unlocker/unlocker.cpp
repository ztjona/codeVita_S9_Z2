/*
31 / 01 / 2021
@author: z_tjona

Tema: Codevita practice
*/

#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define udll unsigned long long

/*===========================================================
DEFS
===========================================================*/
template <typename T = int>
void printMatrix(vector<vector<T>>& matrix, string sep = " ", string endLine = "\n")
{
	for (size_t i = 0; i < matrix.size(); i++)
	{
		for (size_t j = 0; j < matrix[0].size() - 1; j++)
			cout << matrix[i][j] << sep;

		cout << matrix[i].back() << endLine;
	}
}

template <typename T = int>
vector<vector<T>> readMatrix(size_t nRows, size_t nCols)
{
	vector<vector<T>> matrix;

	for (size_t i = 0; i < nRows; i++)
	{
		vector<T> linea;
		for (size_t j = 0; j < nCols; j++)
		{
			T a;
			cin >> a;
			linea.push_back(a);
		}
		matrix.push_back(linea);
	}
	return matrix;
}

// ==========================================================
template <typename T = int>
vector<T> readVector()
{
	vector<T> myVector;

	string line;
	cin.ignore(); // otherwise deads!
	getline(cin, line);

	stringstream parse(line);

	T i;
	while (parse >> i)
		myVector.push_back(i);

	return myVector;
}

enum Direction
{
	Counter_clockwise = -1,
	Clockwise = 1
} direction;

// ==========================================================
template <typename T = int>
void moveLayer(vector<vector<T>>& matrix, size_t idLayer, size_t numRots, Direction dir)
{
	size_t N = matrix.size();
	size_t M = matrix[0].size();
	size_t colsLayer = M - 2 * idLayer;
	size_t rowsLayer = N - 2 * idLayer;

	size_t nLayer = max(colsLayer, rowsLayer);
	size_t numElementsInLayer = 2 * (colsLayer - 1) + 2 * (rowsLayer - 1);

	numRots %= numElementsInLayer;

	if (numRots == 0)
		return;

	// --- there are some rotations
	if (numRots > numElementsInLayer / 2)
	{ // too many rotations in this direction, reversing!
		numRots = numElementsInLayer - numRots;
		if (dir == Direction::Clockwise)
			dir = Direction::Counter_clockwise;
		else
			dir = Direction::Clockwise;
	}

	// --- rotate!
	size_t rUp = idLayer;
	size_t rDown = N - idLayer - 1;
	size_t cLeft = idLayer;
	size_t cRight = M - idLayer - 1;

	int valDownLeft;
	int valUpLeft;
	int valDownRight;
	int valUpRight;

	if (dir == Direction::Counter_clockwise)
	{
		// ---- counter_clockwise
		for (size_t i = 0; i < numRots; i++)
		{
			valDownLeft = matrix[rDown][cLeft];
			valUpLeft = matrix[rUp][cLeft];
			valDownRight = matrix[rDown][cRight];
			valUpRight = matrix[rUp][cRight];
			// --- rotating! (no corners)
			for (size_t j = 0; j < nLayer - 1; j++)
			{
				if (cLeft + j + 1 <= cRight)
				{ // - side up
					matrix[rUp][cLeft + j] = matrix[rUp][cLeft + j + 1];
					// - side down
					matrix[rDown][cRight - j] = matrix[rDown][cRight - j - 1];
				}
				if (rUp + j + 1 <= rDown)
				{
					// - side left
					matrix[rDown - j][cLeft] = matrix[rDown - j - 1][cLeft];

					// - side right
					matrix[rUp + j][cRight] = matrix[rUp + j + 1][cRight];
				}
			}
			// -- completing corners
			matrix[rDown][cLeft + 1] = valDownLeft;
			matrix[rUp + 1][cLeft] = valUpLeft;
			matrix[rDown - 1][cRight] = valDownRight;
			matrix[rUp][cRight - 1] = valUpRight;
		}
	}
	else
	{
		// clockwise
		for (size_t i = 0; i < numRots; i++)
		{ // - saving corners
			valDownLeft = matrix[rDown][cLeft];
			valUpLeft = matrix[rUp][cLeft];
			valDownRight = matrix[rDown][cRight];
			valUpRight = matrix[rUp][cRight];

			// -- rotating!(no corners)
			for (size_t j = 0; j < nLayer; j++)
			{
				if (cLeft + j + 1 <= cRight)
				{
					// - side up
					matrix[rUp][cRight - j] = matrix[rUp][cRight - j - 1];
					// - side down
					matrix[rDown][cLeft + j] = matrix[rDown][cLeft + j + 1];
				}

				if (rUp + j + 1 <= rDown)
				{
					// - side left
					matrix[rUp + j][cLeft] = matrix[rUp + j + 1][cLeft];
					// - side right
					matrix[rDown - j][cRight] = matrix[rDown - j - 1][cRight];
				}
			}

			// -- completing corners
			matrix[rDown - 1][cLeft] = valDownLeft;
			matrix[rUp][cLeft + 1] = valUpLeft;
			matrix[rDown][cRight - 1] = valDownRight;
			matrix[rUp + 1][cRight] = valUpRight;
		}
	}
}

/*===========================================================
MAIN
===========================================================*/
int main()
{
	int N, M;
	cin >> N >> M;

	vector<vector<int>> matrix = readMatrix(N, M);

	vector<size_t> rots = readVector<size_t>();

	size_t numLayers = rots.size();// min(N, M) / 2;

	for (size_t idLayer = 0; idLayer < numLayers; idLayer++)
	{
		if (idLayer % 2 == 0)
			// counter clockwise
			direction = Direction::Counter_clockwise;
		else
			// clockwise
			direction = Direction::Clockwise;

		moveLayer(matrix, idLayer, rots[idLayer], direction);
	}
	printMatrix<int>(matrix);
}

/*===========================================================
FUNCIONES
===========================================================*/

//===========================================================