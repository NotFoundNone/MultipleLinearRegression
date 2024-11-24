import matplotlib.pyplot as plt

def visualize_data(df):
    plt.figure(figsize=(15, 10))

    # Original Data: Price vs GearCount
    plt.subplot(2, 2, 1)
    plt.scatter(df['EngineSpeedRPM'], df['GearCount'], color='blue', label='Original Data')
    plt.xlabel('EngineSpeedRPM')
    plt.ylabel('Price')
    plt.title('Original')
    plt.legend()

    # Min-Max Normalized: Price vs EngineSpeedRPM
    plt.subplot(2, 2, 2)
    plt.scatter(df['EngineSpeedRPM_MinMax'], df['GearCount_MinMax'], color='green', label='Min-Max Normalized')
    plt.xlabel('Engine Speed RPM (Min-Max)')
    plt.ylabel('GearCount (Min-Max)')
    plt.title('Min-Max Normalization')
    plt.legend()

    # Z-Score Normalized: Price vs GearCount
    plt.subplot(2, 2, 3)
    plt.scatter(df['EngineSpeedRPM_Standart'], df['GearCount_Standart'], color='red', label='Z-Score Normalized')
    plt.xlabel('EngineSpeedRPM (Standart)')
    plt.ylabel('GearCount (Standart)')
    plt.title('Standart Normalization')
    plt.legend()

    # Unit Vector Normalized: Price vs EngineSpeedRPM
    plt.subplot(2, 2, 4)
    plt.scatter(df['EngineSpeedRPM_Max'], df['GearCount_Max'], color='purple', label='Unit Vector Normalized')
    plt.xlabel('Engine Speed RPM (Max)')
    plt.ylabel('GearCount (Max)')
    plt.title('Max Normalization')
    plt.legend()

    plt.tight_layout()
    plt.show()
